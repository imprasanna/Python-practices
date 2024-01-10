print(1)
print(2)

try:
    f = open("asdfghjkl;")
except:
    print("The file does not exist!")

print("----------")

try:
    f = open("asdfghjkl;")
except Exception as e:
    print(e)

print("----------")

try:
    f = open("asdfghjkl;")
except FileNotFoundError:
    print("The file does not exist!")
except Exception as e:
    print(e)

print("----------")

try:
    fdsfj; fdsfdsf; fsjdfs
    f = open("asdfghjkl;")
except FileNotFoundError:
    print("The file does not exist!")
except Exception as e:
    print(e)

print("----------")

try:
    fdsfj; fdsfdsf; fsjdfs
    f = open("asdfghjkl;")
except FileNotFoundError:
    print("The file does not exist!")
except Exception as e:
    print(e)
finally:
    print("this message!")

print("----------")

try:
    f = open("test.txt")
except FileNotFoundError:
    print("The file does not exist!")
except Exception as e:
    print(e)
finally:
    print("this message!")   #this statement will be printed no matter what

print("----------")

n = 100
if n == 0:
    raise Exception("n can't be 0!")
if type(n) is not int:
    raise("n must be an int")

print(1/n)

print("----------")

n = 1
assert(n != 0)
print(1/n)

# excpetion --> for error handling
# assertion --> for data verification

# exception can be used to read and handle the exception in a way that the error does not exist
# assertion can be used for checking preconditions, postconditions, etc. for error detection and debugging