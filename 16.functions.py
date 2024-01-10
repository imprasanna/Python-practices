def function1():   #defining a function
    print("hello from function1!")

function1()

print("----------")

function1()

print("----------")

def function2():
    return "hello from function2!"

return_from_function2 = function2()
print(return_from_function2)

function2()

print("----------")

def function3(s):
    print("\t{}".format(s))

function3("parameter")

print("----------")

def function4(s1, s2):
    print("{} {}".format(s1, s2))

function4("any", "thing")
function4(s1="thing", s2="any")
function4(s2="any", s1="thing")

print("----------")

def function5(s1="default"):
    print("{}".format(s1))

function5()
function5("anything")

print("----------")

def function6(s1, *more):
    print("{} {}".format(s1, " ".join([s for s in more])))

function6("function6")
function6("function6", "a")
function6("function6", "a", "b", "c")

print("----------")

#dictionary of arguments
def function7(**ks):
    for a in ks:
        print(a, ks[a])

function7(a="1", b="2", c="3")

print("----------")

def function8(s, f, i, l):
    print(type(s))
    print(type(f))
    print(type(i))
    print(type(l))

function8("string", 1.0, 1, ['l', 'i', 's', 't'])

print("----------")

v = 100    #global variable
print(v)

def function9():
    v = 5      #local variable
    v += 1
    print(v)

function9()
print(v)

print("----------")

def function10():
    global v
    v += 1
    print(v)

function10()

print("----------")

def function11():
    print("hello from function11!")

def function12():
    function11()         #one function calling the other function
    print("hello from function12!")

function12()

print("----------")

#recursive method
def function13(x):
    print(x)
    if x > 0:
        function13(x - 1)
    
function13(5)

print("----------")

#iterative method
def function14(x):
    while x >= 0:
        print(x)
        x -= 1

function14(5)

print("----------")