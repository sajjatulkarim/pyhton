#list is collection which is ordered and changeable. Allows duplicate members.
#list is written with square brackets.
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Add item into the list

thislist.append("orange") #append() method adds an item to the end of the list.
print(thislist) 

thislist.insert(1, "orange") #insert() method inserts an item at the specified index. 1 is index number.
print(thislist)

thislist.extend(["mango", "grapes"]) #extend() method adds the specified list elements (or any iterable) to the end of the current list.
print(thislist)

thislist.remove("banana") #remove() method removes the specified item.
print(thislist) 

thislist.pop(3) #pop() method removes the specified index, (default is the last item). here 3 is index number.

print(thislist)

thislist.clear()      #clear() method removes all the items from the list. Clear method does not delete the list itself, just empties it. and it wont pass any argument.
print(thislist)

#del thislist  #del keyword removes the list completely.
#print(thislist) #it will give error because list is deleted.

#copy() method copies the list. it does not pass any argument.

thislist.insert(0, "grapes")
print(thislist)

thislist.extend(["banana", "cherry", "apple"])
print(thislist)

mylist = thislist.copy()
print(mylist)

#list() method also copies the list.
newlist = list(thislist)
print(newlist)

#count() method returns the number of times the specified item appears in the list.
print(thislist.count("apple"))

#sort() method sorts the list ascending by default. if you want to sort descending order, set the reverse parameter to True.
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)


print(thislist.__sizeof__())#
#sizeof() method returns the size of the list in bytes. it is not a common method to use.