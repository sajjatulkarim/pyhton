def student_name():
    return "John Doe"

print(student_name())
print(type(student_name()))
print(isinstance(student_name(), str))
# This code defines a function that returns a student's name as a string.
# It then prints the name, its type, and checks if it is an instance of str


def student_name():
    return "John Doe", "Jane Smith" # The function is modified to return a tuple of names.

print(student_name())
print(type(student_name()))
print(isinstance(student_name(), str))  # This will now return False since the return type is a tuple, not a string.
# The function now returns a tuple of names, which changes the type check result.