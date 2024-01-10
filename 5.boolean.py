valid = True
not_valid = False

print(valid)
print(not_valid)

print(valid == True)
print(not_valid == True)

print(valid != True)
print(not_valid != True)

print("-------")

print(not valid)
print(not not_valid)

print("-------")

print((10 > 9) == True)
print((10 == 10) == True)
print((10 != 10) == False)
print((10 >= 10) == True)
print((10 <= 10) == True)
print((10 < 9) == True)

print("-------")

print(10 > 9)
print(10 == 10)
print(10 != 10)
print(10 >= 10)
print(10 <= 10)
print(10 < 9)

print("------")

print(10 > 5 and 10 < 5)
print(10 > 5 or 10 < 5)

print("-------")

print(bool(0))
print(bool(1))

print(bool(0) == False)
print(bool(1) == True)

print("-------")

print(10 + 10)
print(10 - 10)
print(10 / 10)
print(10 // 10)
print(10 / 3)
print(10 // 3)
print(10 * 10)
print(10 ** 10)
print(10 % 10)


print("--------")

x = 10
print(x)
x = x + 1
print(x)
x += 1
print(x)
x -= 1
print(x)
x *= 5
print(x)
x /= 5
print(x)

print("--------")

x = 13
print(bin(x))
print(bin(x)[2:].rjust(4, "0"))    #[2:] is for removing 0b in binary

y = 5
print(bin(y)[2:].rjust(4, "0"))

print(bin(x & y)[2:].rjust(4, "0"))
print(bin(x | y)[2:].rjust(4, "0"))

print(bin(x >> 1)[2:].rjust(4, "0"))    #x >> 1 specifies bitwise right shift by 1
print(bin(x >> 2)[2:].rjust(4, "0"))
print(bin(x << 1)[2:].rjust(4, "0"))
