with open('english.txt', 'r', encoding='utf-8') as f:
    eng_to_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    result = []
    for line in f:
        lines = line.rstrip().split(' - ')
        print(lines)
        if lines[0] in eng_to_rus:
            word = eng_to_rus[lines[0]]
            result.append(word + ' - ' + lines[1])
    print(result)
with open('russian.txt', 'w', encoding='utf-8') as f:
    f.writelines("%s\n" % l for l in result)
