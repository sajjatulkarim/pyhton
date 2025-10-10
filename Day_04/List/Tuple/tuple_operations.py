#Tuple is collection which is ordered and unchangeable. Allows duplicate members.
#Tuple is written with round brackets.
#Once a tuple is created, you cannot change its values. Tuples have less functionality than lists. It is immutable.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#thistuple[1] = "orange" #it will give error because tuple is unchangeable.
#print(thistuple)

#But we can convert the tuple into list, change the list and convert it back to tuple.

y = list(thistuple) #convert tuple into list.
y[1] = "orange"     #change the list.
thistuple = tuple(y) #convert the list back into tuple.
print(thistuple)
#we can also add items into the tuple by converting it into list and then back to tuple.