Result = [10,4,3,6,2]
print("Original list:", Result)

# Sort in ascending order using lambda
sorted_result = sorted(Result, key=lambda x: x)
print("Sorted list (ascending):", sorted_result)