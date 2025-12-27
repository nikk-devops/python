
def convert(c, f):
    c = (f - 32) * 5/9
    return c    
f = float(input("Enter temperature in Fahrenheit: "))


c = convert(0, f)
print(f"Temperature in Celsius is {c}") 