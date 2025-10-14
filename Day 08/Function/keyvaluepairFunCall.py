def course(**data): #**data is a keyword variable size argument, you can pass any number of keyword arguments.** represents keyword variable size argument. it stores all the arguments in the form of dictionary.
    for key, value in data.items(): #items() function is used to get the key-value pairs of the dictionary.
        print(f"{key}: {value}")

course(name="Python", duration="3 months", level="Beginner") #function call with keyword variable size argument