'''We can have a value as default as default argument in a function.
If we specify name = “stranger” in the line containing def, this value is used when no
argument is passed.
If we pass an argument, the passed value is used instead of the default value.'''

def greet(name="stranger"):
    gr = "Hello " + name
    return gr   
a = greet()  # No argument is passed
print(a)  # This will print "Hello stranger"    
b = greet("Harry")  # Argument is passed
print(b)  # This will print "Hello Harry"

