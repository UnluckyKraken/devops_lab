num = int(input())
factors = list()
i = 2

while i * i <= num:
    while num % i == 0:
        factors.append(i)
        num = num // i
    i = i + 1
if num > 1:
    factors.append(num)

prime = False
two_digit = False
x = 1
for f in range(len(factors)):
    if len(factors) < 2:
        print('-1')
        prime = True
        break
    if len(str(factors[f])) >= 2:
        print('-1')
        two_digit = True
        break
    if x * factors[f] < 10:
        x *= factors[f]
        counter = f + 1

if not prime and not two_digit:
    factors_string = ''.join(str(elem) for elem in factors)
    x = str(x) + factors_string[counter:]
    print(x)
