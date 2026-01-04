'''
A file is data stored in a storage device. A python program can talk to the file by reading
content from it and writing content to it.
'''

f = open("read.txt", "r")  # Open a file in read mode
data = f.read()       # Read the content of the file
print(data)           # Print the content
f.close()            # Close the file
