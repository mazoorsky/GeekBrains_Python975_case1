positive = int(input('Введи целое положительное число: '))
while positive <= 0:
    positive = int(input('Введи целое положительное число: '))

negative = int(input('Введи целое отрицательное число: '))
while negative >= 0:
    negative = int(input('Введи целое отрицательное число: '))

# Вариант с оператором **:
def power(x, y):
    z = x ** y
    return z

result = power(positive, negative)
print(result)

# Вариант с циклом:
def power_cycle(x, y):
    i = 1
    pow_pos = abs(y)
    result = 1
    while i <= pow_pos:
        result *= x
        neg_result = 1 / result
        i += 1
    return neg_result

res = power_cycle(positive, negative)
print(res)