def s_marks1 (**data):  return{
    'Rahul':{"age":20, "Class": 10, "Location": "Chawkbazar"},'Rajib':{"age":21,"Class": 11, "Location": "Muradpur"},'Raju':{"age":30, "Class": 12, "Location": "Newmarket"}

    }

z = s_marks1()
#print(z)  # Print the dictionary
z_iter = iter(z.values())  # Create an iterator from the dictionary

print(next(z_iter))  # Get the next key from the iterator
#print(next(z_iter))  # Get the next key from the iterator
#print(next(z_iter))  # This will raise StopIteration as there are no more keys
print(next(z_iter))
print(next(z_iter))
#print(next(z_iter))  # This will raise StopIteration as there are no more keys
print("**********")

