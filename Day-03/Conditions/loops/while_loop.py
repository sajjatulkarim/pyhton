#While loop is used when we don't know the number of iterations
# Print all even numbers from the list

a = [20,1,22,3,5,6,9]
result = []
i = 0 #initialization
# condition
while i < len(a):
    if a[i] % 2 == 0:
        result.append(a[i])
    i += 1 # increment
print(result)
    