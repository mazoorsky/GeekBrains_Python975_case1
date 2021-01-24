def cap_word(string):
    string = string.capitalize()
    return string

def cap_words(string):
    string = string.title()
    return string

word = input('Введи слово: ')
print(cap_word(word))

words = input('Введи слова через пробел: ')
print(cap_words(words))