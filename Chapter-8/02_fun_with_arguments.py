'''A function can accept some value it can work with. We can put these values in the
parentheses.
A function can also return value as shown below:'''

def add(a, b):  # a and b are parameters
    c = a + b
    return c  # returning the value
result = add(5, 3)  # 5 and 3 are arguments
print("The sum is:", result)

# Another Example
def greet(name):
    gr = "hello"+ name
    return gr
a = greet ("hannu")
print(a)
# a will now contain "hello harry" 