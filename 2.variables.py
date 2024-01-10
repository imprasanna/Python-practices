name = "oasis"

print(name)

name_length = 5
print(name_length)

name, name_length = "oasis", 5     #this is same

print(type(name))
print(type(name_length))

print(type(True))

#type casting
string = "4"

print(type(string))
print(type(int(string)))

name_list = ["oasis", "prasanna", "kevin", "john"]
print(type(name_list))

name1, name2, name3, name4 = name_list
print(name1)
print(name2)
print(name3)
print(name4)

name_tuple = ("oasis", "prasanna")
print(type(name_tuple))

my_set = {1, 2, 3, 4}
print(type(my_set))

my_variable = None
my_dict = {"name": "John", "age": 30, "city": "New York"}

print(type(my_variable))
print(type(my_dict))