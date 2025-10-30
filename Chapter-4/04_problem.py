# Write a program to sum a list with 4 numbers.

numbers = []
n1 = int(input("Enter number 1: "))
numbers.append(n1)
n2 = int(input("Enter number 2: "))
numbers.append(n2)
n3 = int(input("Enter number 3: "))
numbers.append(n3)
n4 = int(input("Enter number 4: "))
numbers.append(n4)
total = sum(numbers)
print("The sum of the numbers is:", total)
