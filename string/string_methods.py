# String methods in Python states that
# String methods are built-in functions that can be used to perform various operations on strings as in
# String methods are called using the dot (.) operator followed by the method name and parentheses
# String methods do not modify the original string, they return a new string or a value based on the operation performed

# String can be converted to title case using title() method
string = "hello world"
title_case_string = string.title()
print(title_case_string)  # Output: Hello World

# String can be converted to capitalize case using capitalize() method
string = "hello world"  
capitalized_string = string.capitalize()
print(capitalized_string)  # Output: Hello world

# String can be converted to casefolded case using casefold() method
string = "Hello World"  
casefolded_string = string.casefold()
print(casefolded_string)  # Output: hello world

# String can be converted to swapcase using swapcase() method
string = "Hello World"
swapped_case_string = string.swapcase()
print(swapped_case_string)  # Output: hELLO wORLD   

# String can be checked for numeric using isnumeric() method
string = "12345"
is_numeric = string.isnumeric()
print(is_numeric)  # Output: True
string = "123a45"
is_numeric = string.isnumeric()
print(is_numeric)  # Output: False

# String can be checked for decimal using isdecimal() method
string = "12345"
is_decimal = string.isdecimal()
print(is_decimal)  # Output: True
string = "123.45"
is_decimal = string.isdecimal()
print(is_decimal)  # Output: False
string = "123a45"
is_decimal = string.isdecimal()
print(is_decimal)  # Output: False  

# String can be checked for identifier using isidentifier() method. It identifies if the string is a valid identifier (variable name) in Python.It shows if the variable assigning methods are valid or not.  for example:
string = "variable_name"
is_identifier = string.isidentifier()
print(is_identifier)  # Output: True
string = "1variable_name"
is_identifier = string.isidentifier()
print(is_identifier)  # Output: False
string = "variable-name"
is_identifier = string.isidentifier()   
print(is_identifier)  # Output: False
string = "variable name"
is_identifier = string.isidentifier()
print(is_identifier)  # Output: False
string = "variable_name"
is_identifier = string.isidentifier()
print(is_identifier)  # Output: True

# String can be checked for printable using isprintable() method. It checks if all characters in the string are printable or not. It returns True if all characters are printable or the string is empty, otherwise it returns False.
string = "Hello World!" 
is_printable = string.isprintable()
print(is_printable)  # Output: True

string = "Hello\nWorld!"
is_printable = string.isprintable() 
print(is_printable)  # Output: False because \n is not a printable character. It is an escape character that represents a new line.

string = "Hello\tWorld!"
is_printable = string.isprintable() 
print(is_printable) # Output: False because \t is not a printable character. It is an escape character that represents a tab space.



# String can be checked for case using islower() and isupper() methods
string = "hello world"
is_lower = string.islower()
print(is_lower)  # Output: True
string = "Hello World"
is_upper = string.isupper()
print(is_upper)  # Output: False

#But we can convert the string to upper case using upper() method and then check for isupper() method
string = "Hello World"  
upper_string = string.upper()
is_upper = upper_string.isupper()   
print(is_upper)  # Output: True BUT the original string remains unchanged


