# (1) Write a method that returns true when a key is found in a dictionary, false otherwise.
def key_exists(dictionary, key):
    return key in dictionary

# (2)
my_dict = {"name": "john", "age": 30}

print(key_exists(my_dict, "name"))   # True
print(key_exists(my_dict, "city"))   # False