string1 = "I am a string!"
string2 = 'I am a string too!'

print(string1)
print(string2)

print("--------")

string3 = """I am a long
long
string!"""

print(string3)

print("--------")

string4 = "I'm a string"
print(string4)

string5 = 'I\'m also a string'
print(string5)

string6 = "I'm a string\nI'm on a newline!"
print(string6)

print("--------")

string7 = "\\ \x41\x42\x43"    #hexadecimal escape sequence for ASCII characters
print(string7)

print("--------")

string7 = "aaaaaaaaaa"
print(string7)

string7 = "a" * 10
print(string7)

print("--------")

print(len(string7))

print("--------")

print ("a" in string7)
print("string" in string4)
print("all" in string5)

print("--------")

print(string4.startswith("I"))
print(string4.startswith("n"))

print("--------")

print(string4.index("string"))
print(string4.upper())
print(string4.lower())

print("--------")

messy_string = "       Messy string!"
print(messy_string)
print(messy_string.strip())
print(messy_string.replace("!", "?").strip())
print(messy_string.replace("string", "example").strip())
print(messy_string.split())
string8 = "Hello, world, how are you?"
print(string8.split(","))

print("--------")

string8 = "I am a string"
print(string8)
print(string8.encode())
print(string8.encode("utf-8"))

print("--------")

print(string8.rjust(25))
print(string8.rjust(25, "X"))
print(string8.ljust(25))
print(string8.ljust(25, "X"))

print("--------")

print("I am" + "a string")
print("String 8 is " + str(len(string8)) + " characters long")

print("--------")

print(1 + 1)
print("1" + "1")

print(type("1" + "1"))

print("--------")

#format method
print("string4 is {} characters long!". format(len(string4)))
print("{} {} {}".format(len(string4), 5.0, 0x12))

print("{0} {2} {1}".format(len(string4), 5.0, 0x12)) #defining the order

print("{length}".format(length=len(string4)))   #specifying variable with format method

length = len(string4)
print(f"string4 is {length} characters long")   #this is also a way of using the format method

print("string4 is {length:.2f} characters long".format(length=len(string4)))
print("string4 is {length:.3f} characters long".format(length=len(string4)))
print("string4 is {length:.4f} characters long".format(length=len(string4)))
print("string4 is {length:x} characters long".format(length=len(string4)))
print("string4 is {length:b} characters long".format(length=len(string4)))
print("string4 is {length:o} characters long".format(length=len(string4)))

print("--------")

#string formatting using %
print("string4 is %d characters long" % len(string4))
print("string4 is %f characters long" % len(string4))
print("string4 is %x characters long" % len(string4))
print("string4 is %o characters long" % len(string4))

print("--------")

name = "Prasanna"
age = 23
print("My name is %s and I am %d years old!" % (name, age))
