tuple_items = ("item1", "item2", "item3")
print(tuple_items)
print(type(tuple_items))

print("-----")

tuple_numbers = (1, 2, 3)
print(tuple_numbers)
print(type(tuple_numbers))

print("------")

tuple_repeat = ("Combine",) * 4
print(tuple_repeat)
print(type(tuple_repeat))

print("------")

mixed_tuple = ("A", 1, ("A", 1))
print(mixed_tuple)
print(type(mixed_tuple))

print("-------")

tuple_combined = tuple_items + tuple_numbers
print(tuple_combined)
print(type(tuple_combined))

print("-------")

item1, item2, item3 = tuple_items
print(item1)
print(item2)
print(item3)


print("--------")

print("item2" in tuple_items)
print("item3" in tuple_items)
print("item4" in tuple_items)

print("--------")

print(tuple_items.index("item2"))

print("--------")

tuple_items = ("item1", "item2", "item3")
print(tuple_items[0])
print(tuple_items[1])
print(tuple_items[2])

print("--------")

print(len(tuple_items))

print("--------")

print(tuple_items[-1])
print(tuple_items[-2])
print(tuple_items[-3])

print("--------")

#Slicing items
print(tuple_items[0:2])     #slicing from index 0 to 2, gives items form 0 to 1 index
print(tuple_items[:2])      #similar to slicing form index 0 to 2
print(tuple_items[-3:-1])

print(tuple_items[0:2])
print(tuple_items[:2])
print(tuple_items[-3:-1])

print("--------")

#slicing strings
string1 = "I am a string"
print(string1[0:4])
print(string1[:-1])
