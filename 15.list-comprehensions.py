list1 = ["a", "b", "c"]
print(list1)

print("----------")

list2 = [x for x in list1]
print(list2)

print("----------")

list3 = [x for x in list1 if x == 'a']
print(list3)

print("----------")

list4 = [x for x in range(5)]
print(list4)

print("----------")

list5 = [hex(x) for x in range(5)]
print(list5)

print("----------")

list6 = [hex(x) if x > 0 else 'X' for x in range(5)]
print(list6)

print("----------")

list7 = [x * x for x in range(5)]
print(list7)

print("----------")

list8 = [x for x in range(5) if x == 0 or x == 1]
print(list8)

print("----------")

list9 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list9)

print("----------")

list10 = [y for x in list9 for y in x]         #create a list of y from the nested list x and create a new list of each y that are in x
print(list10)

print("----------")

set1 = {x + x for x in range(5)}
print(set1)

print("----------")

list11 = [c for c in "string"]
print(list11)

print("----------")

print("". join(list11))
print("-".join(list11))

print("----------")

list12 = []
for c in "string":
    list12.append(c)
print(list12)