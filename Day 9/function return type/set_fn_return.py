def month ():
    janurary = {20,30,21}
    february = {28,29}
    march = {30,31,21}
    return janurary, february, march
print(month())
print(type(month()))

x = month()
print(x)

for i in x:
    print(i)
    print(type(i))