def greeting(username):
    print(f"Hello, {username}")
    
#greeting() #function call without argument will raise an error
greeting("Alice") #function call with argument

def add(a, b):
    print(a + b)
    
add(3, 5)

def greeting_with_default(username="Guest"):
    print(f"Hello, {username}")
    
greeting_with_default() #uses default value