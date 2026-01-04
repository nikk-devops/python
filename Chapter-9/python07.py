'''
Write a program to find out the line number where python is present from ques 6.
'''
with open("test.txt", "r") as f:
    content = f.read()
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if "python" in line:
            print(f"The word 'python' is present in line {i+1}.")

            