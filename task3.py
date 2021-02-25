a = input()
b = list()
x = str()

for i in a.split():
    b.append(i[::-1])

x = ' '.join(b)
print(x)
