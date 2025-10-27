you = open ("mytext.txt", "r")
content = you.read()
print(content)
you.close()

print(you.closed)