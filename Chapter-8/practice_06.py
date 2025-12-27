#Write a python function which converts inches to cms

def convert(inches):
    cms = inches * 2.54
    return cms
inches = float(input("Enter length in inches: "))
cms = convert(inches)
print(f"Length in centimeters is {cms} cm")
