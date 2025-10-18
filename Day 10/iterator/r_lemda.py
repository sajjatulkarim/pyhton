#def sqr(x):
  #  return x**2

#print(sqr(4))


y = lambda x: x**2

print(y(4))

num = [ 1,2,3,4]
sq_num = list(filter(lambda x:x%2==0,num ))
print(f"{sq_num}")

num = [40,50,60,71]
sq_num = list(map(lambda x:x%2==0,num ))
print(f"{sq_num}")