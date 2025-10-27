you = open("mytext.txt", "w")
you.write("Hello World")

you.write("\nWelcome to File Handling in Python.")
you.write("\nThis is line 1. \nThis is line 2. \nThis is line 3.")
you.close() 


print(you.closed)