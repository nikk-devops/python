# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program

a = "Make a lot of money"
b = "buy now"
c = "subscribe this"
d = "click this"

message = input("Enter the message: ")

if (a in message) or (b in message) or (c in message) or (d in message):
    print("This is a spam message.")
else:
    print("This is not a spam message.")

    