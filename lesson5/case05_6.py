with open('subjects.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lines = line.split(':')
        print(lines)
