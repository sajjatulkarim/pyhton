string ="Hello World"

def upper_str(string):
    return string.upper()
mapped_str = map(upper_str, string)
#print (list(mapped_str))

#Output: ('H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D')

out = " ".join (mapped_str)
print(out)