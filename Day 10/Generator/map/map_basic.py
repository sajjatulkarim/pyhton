#Map is method used for implement a function to each item in an iterable (list, tuple etc.)
#The map() function returns a map object (an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
#Syntax: map(function, iterable, ...)
#Example 1: Using map() to double each item in a list

lst = [1, 2, 3, 4, 5]



#lst1 = list(map(square_lst, lst))

#print(lst1)

#lst1 =[30,32,34,36,38]

def sq (x):
    return x**2
lst1 = list(map(sq, lst))
print(lst1)