
n = int(input("Enter a number: "))
items = []
for i in range (1,n+1):
    
    item = int(input("Enter item: "))
    


   
    items.append(item)

print(items)

for i in range (0, n):
    
    if items[i] % 2 == 0: #
        print(f"{items[i]} is even")
    else:
        print(f"{items[i]} is odd")
        


    
    
    
    