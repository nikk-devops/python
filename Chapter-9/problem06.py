'''
Write a program to make a copy of a text file “this. txt”
'''

with open("this.txt") as f:
    content = f.read()

with open("copy_of_this.txt", "w") as f2:
    f2.write(content)
        