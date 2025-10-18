def marks():
    return 10.5 # single value will return as float

print(marks())
print(type(marks()))

def marks():
    return 10.5, 3.4

print(marks())
print(type(marks())) # returns as tuple