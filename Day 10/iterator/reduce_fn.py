import functools
lst =[1,2,3,4,5]
sum = functools.reduce(lambda a,b:a+b,lst)
print(sum)