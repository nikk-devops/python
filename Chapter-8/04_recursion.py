'''Recursion is a function which calls itself.
It is used to directly use a mathematical formula as function'''

def factorial(n):
    '''This function returns the factorial of a number'''
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)   
num = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {num} is {factorial(num)}")

