#File is used to store data permanently in a storage device
#File Handling in Python ensure 3 mode of data handling
#1. Read(r) - Default mode, used to read data from a file
#2. Write(w) - Used to write data to a file, if file not present it creates a new file
#3. Append(a) - Used to add data to the end of a file, if file not present it creates a new file
#4. Additional modes - r+, w+, a+ (read and write modes)
#File handling requires opening a file, performing operations and closing the file
#Opening a file
file = open("./File Handeling/todolist.txt", "r")  # Open a file in read mode
content = file.read()          # Read the content of the file
print(content) #Print the content  
file.close()

#Writing to a file
file = open("./File Handeling/todolist.txt", "a")  # Open a file in append mode
file.write("5.Complete Module 7")  # Write data to the file
file.close()

file = open("./File Handeling/todolist.txt", "r")  # Open a file in read mode

content2 = file.read()
print(content2)


file.close()


with open("./File Handeling/todolist.txt", "w") as file:  # Using 'with' to open a file
    file.write("19-10-25\n1. Create ICT practice sheet\n2. Print tracker \n3. going to buy project things\n4. Complete the Python project\n")  # Write data to the 
    #file is automatically closed after the with block
with open("./File Handeling/todolist.txt", "r") as file:
    content3 = file.read()
    print(content3)
    

#Using readlines() to read lines into a list
with open("./File Handeling/todolist.txt", "r") as file:
    lines = file.readlines()  # Read lines into a list
    for line in lines:
        print(line.strip())  # Print each line without extra newlines   
#Using readline() to read a single line
with open("./File Handeling/todolist.txt", "r") as file:
    first_line = file.readline()  # Read the first line
    print("First line:", first_line.strip())  # Print the first line without extra newline  
    second_line = file.readline()  # Read the second line
    print("Second line:", second_line.strip())  # Print the second line without extra newline
    #stripe is used to remove extra newlines and spaces
    #strip() can also remove spaces from the start and end of a string
    #strip means