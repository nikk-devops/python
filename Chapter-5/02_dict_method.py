# PROPERTIES OF PYTHON DICTIONARIES
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys.

# Dictionary is a collection of keys-value pairs.

dict1 = {
    "Hannu": 5,
    "Akshu": 1,
    "Mikku": 6,
    "Pihu": 3,
    "Panchi": 3
}

print(dict1)
print(dict1["Hannu"])  # Accessing value using key
print(dict1.items())  # Returns a list of key-value pairs
print(dict1.keys())  # Returns a list of keys
print(dict1.values())  # Returns a list of values
print(len(dict1))  # Returns the number of key-value pairs in the dictionary
dict1["Akshu"] = 4  # Modifying value of existing key
print(dict1)
dict1["NewKey"] = 10  # Adding a new key-value pair
print(dict1)
del dict1["Pihu"]  # Deleting a key-value pair
print(dict1)
dict1.clear()  # Clearing the dictionary
print(dict1)
del dict1  # Deleting the dictionary entirely
#print(dict1)  # This will raise an error as dict1 is deleted