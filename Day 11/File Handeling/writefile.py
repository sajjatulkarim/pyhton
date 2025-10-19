#Write mode in python is used to write data to a file
#If the file already exists, it will overwrite the existing content


with open("./File Handeling/writetodolist.txt", "w") as file:
    file.write("20-10-25\n1. Going to Zara's Home\n2. Take classes  \n3. Set for Module\n4.Set for QA project\n")  # Write data to the 
    #file is automatically closed after the with block


with open("./File Handeling/writetodolist.txt", "w") as file:
    file.write("19-10-25\n1. Create ICT practice sheet\n2. Print tracker \n3. going to buy project things\n4. Complete the Python project\n")  # Write data to the
    