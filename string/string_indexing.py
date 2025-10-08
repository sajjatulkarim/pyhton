#string indexing is used to access individual characters in a string using their position (index)
#string indexing starts from 0 for the first character, 1 for the second character, and so on
#negative indexing starts from -1 for the last character, -2 for the second last character, and so on. It is used only in python. negative indexing is not available in other programming languages like C, C++, Java, etc.
my_string = "Hello, World!"
first_char = my_string[0] # first character is 'H'
second_char = my_string[1] # second character is 'e'

last_char = my_string[-1] # last character is '!'
second_last_char = my_string[-2] # second last character is 'd'

print("First character:", first_char)
print("Second character:", second_char)     
print("Last character:", last_char)
print("Second last character:", second_last_char)


last_char = my_string[len(my_string)-1] # last character is '!' it is recommended to use negative indexing to access last character hence this line is just for understanding purpose
print("Last character using len():", last_char)