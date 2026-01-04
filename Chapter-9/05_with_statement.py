#we can use normal file functions like:

f = open("read.txt", "r")  # Open a file in read mode
data = f.read()       # Read the content of the file
print(data)           # Print the content
f.close()            # Close the file

#We have an alternative way of handling files using 'with' statement
with open("read.txt", "r") as f:
    data = f.read()
    print(data) 
#No need to explicitly close the file, it will be closed automatically
