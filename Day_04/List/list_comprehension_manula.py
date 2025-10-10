num = int(input("Enter a number: "))

result = []

for i in range(1,num+1):
    item = int(input("Enter item: "))
    
    result.append(item)
for j in result:
    if j % 2 == 0:
        k = j**2
        new_result = []
        new_result.append(k)
        
    else:
        result.append(j)
print(result)
    