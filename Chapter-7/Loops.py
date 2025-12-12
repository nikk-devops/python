# Sometimes we want to repeat a set of statements in our program. For instance: Print 1
# to 1000.
# Loops make it easy for a programmer to tell the computer which set of instructions to
# repeat and how!
# TYPES OF LOOPS IN PYTHON
# Primarily there are two types of loops in python.
# • while loops
# • for loops
# We will look into these one by one.
# WHILE LOOP
# Syntax:
# while (condition): # The block keeps executing until the condition is true
# #Body of the loop
# In while loops, the condition is checked first. If it evaluates to true, the body of the loop
# is executed otherwise not!
# If the loop is entered, the process of [condition check & execution] is continued until
# the condition becomes False.

# Write a program to print 1 to 50 using a while loop.

i = 1
while (i<=50):
    print(i)
    i +=1
    