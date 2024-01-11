#lambdas are anonymous function without name
#lambdas can have any number of arguments like normal function but it can only have one expression

add_4 = lambda x : x + 4
print(add_4(4))

print("-----------")

add = lambda x, y: x + y
print(add(10,4))

def addf(x, y):
    return x + y
print(addf(10, 4))

print("-----------")

print((lambda x, y : x + y)(10, 4))

print("-----------")

is_even = lambda x : x % 2 == 0
print(is_even(2))
print(is_even(3))

print("-----------")

blocks = lambda x, y : [x[i:i+y] for i in range(0, len(x), y)]
print(blocks("string", 2))

print("-----------")

#ord function is used to retrun the unicode code point for any given character
to_ord = lambda x : [ord(i) for i in x]
print(to_ord("aBcD"))

#alternatively using function:
def to_ord2(x):
    ret = []
    for i in x:
        ret.append(ord(i))
    return ret

print(to_ord2("aBcD"))
#here, outcome is the same but we have achieved the same code using lambda in on line
