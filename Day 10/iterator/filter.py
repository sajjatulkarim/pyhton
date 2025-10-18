#Filter function take two arguments,function and iterable
#The function is applied to each item of the iterable and only those items for which the function
#It only returns boolean are included in the result.
num = [ 1,2,3,4]
sq_num = list(filter(lambda x:x%2==0,num ))
print(f"{sq_num}")