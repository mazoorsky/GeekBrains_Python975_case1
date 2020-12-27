def user_data(name, last_name, birth_year, location, email, phone):
    user = f'{name}, {last_name}, {birth_year}, {location}, {email}, {phone}'
    return user

name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
birth_year = input('Введите год рождения: ')
location = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')

print(user_data(name, last_name, birth_year, location, email, phone))