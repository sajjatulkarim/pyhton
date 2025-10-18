def student (): return {
    "Rahim": 21,
    "Karim": 22,
    "Salam": 23
}

s_info = student()
s_iter = iter(s_info.items())
print(next(s_iter)) 
print(next(s_iter))# Output: "Rahim"