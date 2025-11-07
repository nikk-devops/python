# Write a program which finds out whether a given name is present in a list or not.

l = ["Hannu", "Akshu", "Mikku", "Pihu", "Panchi"]
name = input("Enter the name to be searched: ")
if(name in l):
    print(f"{name} is present in the list.")
else:
    print(f"{name} is not present in the list.")
    