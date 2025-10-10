a = {2,4,6,8,10,17}
b = {1,3,5,7,9,2,4,6}

c = a.union(b) # all unique elements in both sets
print(c)
d = a.intersection(b) # common elements in both sets
print(d)

e = a.difference(b) # elements in a but not in b
print(e)
f = a.symmetric_difference(b) # elements in a and b but not in both
print(f)
g = a.issubset(b) # check if a is subset of b
print(g)
h = a.issuperset(b) # check if a is superset of b   
print(h)
i = a.isdisjoint(b) # check if a and b have no elements in common
print(i)
j = a.copy() # copy of set a
print(j)
k = a.clear() # clear all elements in set a
print(k)
l = a.add(12) # add element to set a
print(l)


n = a.pop() # remove and return an arbitrary element from set a
print(n)
