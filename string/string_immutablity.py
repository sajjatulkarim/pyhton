#String immutablityy
# Strings are immutable, meaning once a string is created, it cannot be changed.
my_string = "Hello, World!"
# Attempting to change a character in the string will result in an error
# my_string[0] = 'h' # This will raise a TypeError: 'str' object does not support item assignment
 
#code
#my_string [0] = 'h' # This will raise a TypeError: 'str' object does not support item assignment
print(my_string)

# To change a string, you need to create a new string
new_string = 'h' + my_string[1:] # 'h' + 'ello, World!' = 'hello, World!'. [1:] is slicing which gives string from index 1 to end
print(new_string) # Output: 'hello, World!' 