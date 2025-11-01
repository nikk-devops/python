# PROPERTIES OF SETS
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values

set1 = {1, 2, 3, 4, 5, 5, 6, 7, 8, 8}
s = set() # Creating an empty set

print(set1)  # Duplicates will be removed
set1.add(9)  # Adding an element to the set 
print(set1)
set1.remove(3)  # Removing an element from the set
print(set1)
set1.discard(10)  # Removing an element that is not present (no error)
print(set1)
set1.pop()  # Removes and returns an arbitrary element from the set
print(set1)
print(len(set1))  # Returns the number of elements in the set
set1.clear()  # Clears the set
print(set1)
del set1  # Deletes the set entirely
#print(set1)  # This will raise an error as set1 is deleted

s1 = {1, 2, 3}
s2 = {3, 2, 3}

print(s1.union(s2))  # Returns a new set with elements from both sets
print(s1.intersection(s2))  # Returns a new set with elements common to both sets
print(s1.difference(s2))  # Returns a new set with elements in s1 but not in s2
print(s1.issubset(s2))  # Checks if s1 is a subset
print(s1.issuperset(s2))  # Checks if s1 is a superset
print(s1.isdisjoint(s2))  # Checks if s1 and s2 have no elements in common
s1.update(s2)  # Updates s1 with elements from s2
