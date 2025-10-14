def total (*marks): #*marks is a variable size argument, you can pass any number of arguments.* represents variable size argument. it stores all the arguments in the form of tuple. under * marks any keyword can be used.
    print("Total Marks:", sum(marks)) #sum() function is used to calculate the sum of all the elements in the tuple.
total(85, 90, 78, 92,100) #function call with variable size argument
