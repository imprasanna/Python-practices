f = open('top-100.txt')
print(f)

f = open('top-100.txt', 'rt')
print(f)

print("--------")

print(f.readlines())

print("--------")

print(f.readlines())

print("--------")

f.seek(0)      #shifts the current file position back the the start
print(f.readlines())

f.seek(0)
for line in f:
    print(line.strip())

f.close()

print("--------")

f = open("test.txt", "w")
f.write("test line!")
f.close()

print("--------")

f = open("test.txt", "a")
f.write("\ntest line!")
f.close()

print("--------")

print(f.name)
print(f.closed)
print(f.mode)

print("--------")

# #working with rockyou.txt
# with open("rockyou.txt", encoding="latin-1") as f:
#     for line in f:
#         pass     #don't do anything in the file