#Dictionary is a type of data structure that work as key value pair
#some example of dictionary

customer_details = list({'name': "Nihat", 'age' : 25, 'is_verified': True})
print(customer_details) #list function convert dictionary to list of keys
print(customer_details[2]) #accessing first key of dictionary
print(type(customer_details))

customer_details = dict(name= "Nihat", age = 25, is_verified = True)
print(customer_details) #dict function convert key value pair to dictionary
print(customer_details['name']) #accessing value by key
print(type(customer_details))

fruits = {'apple': 5, 'banana': 8, 'orange': 12}
for i in fruits:
    print(i) #print all keys of dictionary
    
for i in fruits.values():
    print(i) #print all values of dictionary
for i in fruits.items():
    c = i
    
    print(i) #print all key value pairs of dictionary as tuple
    
    #zip function can be used to convert two list to dictionary
keys = ['name', 'age', 'is_verified']
values = ['Nihat', 25, True]
customer_details = dict(zip(keys, values))
print(customer_details)