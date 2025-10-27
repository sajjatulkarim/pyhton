from io import UnsupportedOperation


with open("mytext.txt", "a") as file:
    file.write("\nI loving to learn file exception handeling\n")
    
    try:
        print(file.read())
    except: UnsupportedOperation()
    print("You cant read while append or write a file")
    
with open("mytext.txt","r") as file2:
    print(file2.read())
    