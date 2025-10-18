#Lambda is an anonymous function
#It can take any number of arguments but can only have one expression
#Lambda function is used when we need a small function for a short period of time.
#It is often used as an argument to higher-order functions (functions that take in other functions as arguments)

#Syntax: lambda arguments: expression

def square(x):
    return x * x
print(square(5))  #function call


#Using lambda function
square_lambda = lambda x: x * x

print(square_lambda(5))  #function call