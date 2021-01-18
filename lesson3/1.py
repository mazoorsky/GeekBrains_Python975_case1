a = int(input('Введи первое число: '))
b = int(input('Введи второе число: '))

def division_func(x, y):
    while y == 0:
        print('Мы на ноль не делим')
        y = int(input('Введи второе число: '))
    else:
        return x / y

result = division_func(a, b)
print(result)