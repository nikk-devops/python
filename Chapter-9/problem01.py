'''Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’. '''

f = open("poem.txt", "r")  # Open the file in read mode
content = f.read()

if ("twinkle" in content):             # Read the content of the file
    print("The word 'twinkle' is present in the file.")
else:
    print("The word 'twinkle' is not present in the file.")
f.close()            # Close the file

