with open('numbers.txt', 'w', encoding='utf-8') as f:
    f.write(input('Введи числа через пробел: '))

with open('numbers.txt', 'r') as f:
    data = f.readline()
    data_list = [int(x) for x in data.split()]
    print(sum(data_list))
