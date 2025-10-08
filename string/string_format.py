input_name =input("Enter your name: ")
input_place = input("Enter your place: ")
str = "Hello, {}. Welcome to {}!".format(input_name, input_place) #Here we are using format() method. It is used to format the string. {} is a placeholder. Whreever we put {} in the string, it will be replaced by the value passed in format() method.
print(str)

#Another way to format the string is by using f-strings. It is available in Python 3.6 and above.
str2 = f"Hi, {input_name}. Welcome to {input_place}!" #Here we are using f-strings. It is used to format the string. {variable_name} is a placeholder. Whreever we put {variable_name} in the string, it will be replaced by the value of the variable. 
print(str2)