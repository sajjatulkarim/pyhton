with open("filehandeling.txt", "w") as content:
    content.writelines(["File handeling is method to access over context in existing file or it will create a context to extract data or do some functionality","\nWe are dealing with 3 mode for modifying the context we are working on.They are-",  "\n1. Write mode", "\n2. Read mode", "\n3. Append mode"])
    
    content.write("\nWrite mode is deal with write something into a defined location." "\nIf we dont have any existing file where we can write context so before that we can create it." "\nSyntext: (Basic)- Context(variable name) = file name then mode name." "Call write function" "\nEnter the context" "\nclose the file by calling a defined function close()")
    