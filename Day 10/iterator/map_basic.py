lst = [2,3,4,5,6]
for i in lst:
    print(i**2)

num = [40,50,60,71]
sq_num = list(map(lambda x:x%2==0,num ))
print(f"{sq_num}")