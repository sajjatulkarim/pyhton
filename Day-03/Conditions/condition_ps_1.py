# Write a program that takes a number as input and checks whether it is positive, negative, or zero.
X = input("Enter a number: ")
try: #try to convert input to integer
    num = int(X)
    print("You entered an integer.")
except ValueError: #if it fails, convert input to float
    num = float(X)
    print("You entered a float.")
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
    
    
    #simple version
# num = float(input("Enter a number: "))    
# if num > 0:
#     print("The number is positive.")
# elif num < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")
print("Program ended.")