# A for loop is used to iterate through a sequence like list, tuple, or string [iterables]


# Syntax:

l = [1, 7, 8]
for item in l:
    print(item) # prints 1, 7 and 8

# RANGE FUNCTION IN PYTHON

# The range() function in python is used to generate a sequence of number.
# We can also specify the start, stop and step-size as follows:
# range(start, stop, step_size)
# # step_size is usually not used with range()

# Example 1: Print numbers from 0 to 9

for i in range(10):
    print(i)

#FOR LOOP WITH ELSE

l= [1,7,8]
for item in l:
    print(item)
else:
    print("done") # this is printed when the loop exhausts!    

#THE BREAK STATEMENT

# ‘break’ is used to come out of the loop when encountered. It instructs the program to –
# exit the loop now.

for i in range (0,80):
    print(i) # this will print 0,1,2 and 3
    if (i==3):
        break

#THE CONTINUE STATEMENT

# ‘continue’ is used to stop the current iteration of the loop and continue with the next
# one. It instructs the Program to “skip this iteration”.    

for i in range(10):
    print("printing")
    if i == 2: # if i is 2, the iteration is skipped
        continue
print(i)

#PASS STATEMENT

# ‘pass’ is a null statement in python. It is used when a statement is required
# syntactically but we do not want any command or code to execute.  
for i in range(5):
    pass  # No operation is performed here
print("Hello World")  # This will print normally
