with open('kolkhoz_punk.txt', 'r', encoding='utf-8') as f:
    row_count = 0
    for line in f:
        row_count += 1
        size = len(line.split())
        print(f'Строка: "{line.rstrip()}", слов в строке: {size}')

print(f'Всего строк: {row_count}')
