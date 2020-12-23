# объявление переменных и их вывод с типом данных

name = input("Как тебя зовут? ")
age = int(input("Сколько тебе лет? "))
division = 6 / 8
a = 1
b = 2.5

print(type(name), name, type(age), age, type(division), division, type(a == b), (a == b), sep="\n")