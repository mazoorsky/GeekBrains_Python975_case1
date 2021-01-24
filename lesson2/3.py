month = int(input('Введи номер месяца: '))

winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]

while month <= 0 or month > 12:
    month = int(input('Введи номер месяца: '))

if month in winter:
    print('Это зима')
elif month in spring:
    print('Это весна')
elif month in summer:
    print('Это лето')
elif month in fall:
    print('Это осень')