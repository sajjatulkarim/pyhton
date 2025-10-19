with open ("./File Handeling/todolist.txt", "r") as file:
    content = file.read()
    print(content)
    
with open ("./File Handeling/todolist.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip()) 
        
with open ("./File Handeling/todolist.txt", "r") as file:
    first_line = file.readline()
    print("First line:", first_line.strip())
    second_line = file.readline()
    print("Second line:", second_line.strip())