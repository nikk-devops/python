#Write a recursive function to calculate the sum of first n natural numbers.

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1) 
num = int(input("Enter a natural number: "))
print(f"The sum of first {num} natural numbers is {recursive_sum(num)}")    

