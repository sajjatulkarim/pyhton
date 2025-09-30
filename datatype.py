a = 5.3
b= 100
c = "Hello"
d = True
e = None
print(type(a))
print(type(b))  
print(type(c))
print(type(d))
print(type(e))
print(a)
print(b)
print(c)
print(d)
print(e)
print(a+b)
print(c+" World")
print(str(a)+" World")
print(c*3  )
print(a*3)



# print(a+c) # This will give error because we cannot add string and float
print(str(a)+c) # This will work because we are converting float to string
print(a+int(b)) # This will work because we are converting float to int
print(int(a)+float(b) )# This will work because we are converting float to int
    