s_mark = {10,20,30,33,29}
for i in s_mark:
    print(i)
    
#for k,v in s_mark.items():
 #   print(f"{k}:{v}")
    #through error because set does not have key and value pair and iterabale
    print("**********")
s_mark1= {10,20,30,40}
s_mark1_iter = iter(s_mark1) #iter is a build in function which return an iterator object
print(next(s_mark1_iter)) #next is a build in function which return the next value from the iterator object
print(next(s_mark1_iter))
print(next(s_mark1_iter))
print(next(s_mark1_iter))

#print(next(s_mark1_iter)) #stop iteration error because there is no more value in the iterator object

#using for loop we can iterate through the iterator object and show the value randomly since set is not iterable like indexing.
for i in s_mark1_iter:
    print(i) 
