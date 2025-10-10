input_charecter = input("Enter a charecter: ")

if  (input_charecter>='a' and input_charecter <'z'): 
    next_character = chr (ord (input_charecter) + 1)
    print (next_character)

elif (input_charecter == 'z'):
    print("Next charecter is a")

elif (input_charecter >='A' and input_charecter <'Z'):
    next_character = chr (ord (input_charecter) + 1)
    print (next_character)
    
elif (input_charecter == 'Z'):
    print("Next charecter is A")
else:
    print('Not an alphabet')