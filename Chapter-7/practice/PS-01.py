#Write a program to print multiplication table of a given number using for loop

n = int(input("Enter the table you want to write: "))

for i in range(0, 11):
    print(f"{n} x {i} = {(n)*(i)}")