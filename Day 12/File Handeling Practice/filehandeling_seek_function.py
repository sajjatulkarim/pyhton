with open ("filehandeling1.txt","w") as content:
    content.write("File handeling is method to access over context in existing file or it will create a context to extract data or do some functionality." "Methods are -" "\n1. tell(): use to tell where to star reading the content" "\n2. seek(): use to move the pointer across the content." "\n3. truncate():c ")

    

    
    
 
with open ("filehandeling1.txt","r+") as content:
    content.seek(0)
   
    
    content.truncate(10)
    print(content.read())