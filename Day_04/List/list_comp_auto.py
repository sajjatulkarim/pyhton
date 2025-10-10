num = int(input("Enter a number: "))

result = []

for i in range(1,num+1):
    item = int(input("Enter item: "))
    
    result.append(item)
    
    new_result = [k**2 if k%2 == 0 else k for k in result]
print(new_result)