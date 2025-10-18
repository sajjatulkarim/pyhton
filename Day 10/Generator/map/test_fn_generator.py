def mark():
    
    marks =[]
    for i in range(20):
         marks.append(i)
         yield marks[0:5]

out = mark()
print(next(out)) 
print(next(out)) 
print(next(out)) 
print(next(out)) 
print(next(out)) 
print(next(out)) 
print(next(out)) 

# This will print the actual list
   # বড় dataset
#lst = [x for x in range(100)]
#def data_loader(chunk_size, lst):
    #for i in range(0, len(lst), chunk_size):


        #yield lst[i:i + chunk_size]
        
