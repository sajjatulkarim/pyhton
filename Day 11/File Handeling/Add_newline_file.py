lst = ["1. Buy groceries\n", "2. Call Mom\n", "3. Finish homework\n"]
with open ("./File Handeling/writetodolist.txt", "a") as file:
    file.writelines(lst)  # Append data to the file
   