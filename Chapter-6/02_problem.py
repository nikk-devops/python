# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))
total = s1 + s2 + s3
if (total/3)>=40 and s1>=33 and s2>=33 and s3>=33:
    print("Congratulations! You have passed the exam.")
else:
    print("Sorry! You have failed the exam.")
            