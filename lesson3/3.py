def sum_of_max(x,y,z):
    if x < y:
        min = x
    else:
        min = y
    if z < min:
        min = z
    sum = x + y + z - min
    return sum

first = int(input('Первое число: '))
second = int(input('Второе число: '))
third = int(input('Третье число: '))

result = sum_of_max(first, second, third)
print(result)
