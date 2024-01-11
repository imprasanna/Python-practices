import sys

print(sys.version)
print(sys.executable)
print(sys.platform)

print("--------------")

for line in sys.stdin:
	if line.strip()  == "exit":
		break
	sys.stdout.write(">> {}".format(line))

#sys is used because it has lower level functions which can be more difficult to use from exisitng python function
#eg. sys can be used to force python to flush out buffer (python will write everything currently in the buffer directly in the terminal rather than waiting for certain data or character)

print("--------------")

#using sys
for i in range(1, 5):
	sys.stdout.write(str(i))
	sys.stdout.flush()

print("--------------")

#standard method
for i in range(1, 5):
	print(i)

print("--------------")

import time

for i in range(0, 51):
	time.sleep(0.1)
	sys.stdout.write("{} [{}{}]\r".format(i, '#'*i, '.'*(50-i)))
	sys.stdout.flush()
sys.stdout.write("\n")

print("--------------")

print(sys.argv)

print("--------------")

if len(sys.argv) != 3:
	print("[X] To run {} enter a username and password".format(sys.argv[0]))
	sys.exit(5)     #5 is error code

username = sys.argv[1]
password = sys.argv[2]

print("{} {}".format(username, password))

print("--------------")

print(sys.path)

print("--------------")

print(sys.modules)

print("--------------")

#view the official sys docs at docs.python.org