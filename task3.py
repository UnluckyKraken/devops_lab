a = input()
b = list()

for i in a.split():
    b.append(i[::-1])

x = ' '.join(b)
print(x)
