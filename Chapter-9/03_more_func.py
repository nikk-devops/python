
f = open("read.txt", "r")  # Open a file in read mode
line = f.readlines()       # Read the content of the file
print(line)
f.close()            # Close the file

#creating this program in the loop
f = open("read.txt", "r")
line = f.readline()
while (line!=""):
    print(line)
    line = f.readline()
f.close()



