a = list(range(-10,0))
print(a)
b = list(range(10))
print(b)
c = list(range(1,10,2))
print(c)
d = list(range(10,0,-1))
print(d)

# Slicing examples with lists can be implemented similarly in this way:
nums = [10, 20, 30, 40, 50, 60]
print(nums[0:4])   # middle slice
print(nums[-3:-2])   # last 3
print(nums[::2])   # step slice
print(nums[::-1])  # reverse
print(nums[:-3])  # from start to -3
print(nums[3:])   # from index 3 to end
print(nums[:3])   # first 3