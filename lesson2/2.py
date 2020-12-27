text = input('Введите чего-нибудь через пробел: ')
text = list(text.split())

i = 0
while i < len(text) - 1:
    j = i + 1
    text[i], text[j] = text[j], text[i]
    i += 2

print(text)