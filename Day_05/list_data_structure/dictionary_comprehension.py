digit = list(range(1,11))

squared = {x: x*x  if x%2==0 else x for x in digit} #dictionary comprehension   
print(squared)
 