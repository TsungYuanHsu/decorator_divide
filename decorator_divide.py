def decorate_divide(func):
    def inner(n, d):
        if d == 0:
            return 0
        else:
            print(func(n, d)) 
    return inner


@decorate_divide # divide = decorate_divide(divide)
def divide(n, d):
    return n / d

print('Calculate n/d')
d = int(input('Please insert denominator d: '))
n = int(input('Please insert numerator n: '))
if d == 0:
    print(divide(n, d))
else:
    print('Result is')
    divide(n, d)