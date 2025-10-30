# Check ifa tuple type cannot be changed in python.
test = (1, 2, "hannu", 4.5)

test[2] = "John"  # This should raise a TypeError