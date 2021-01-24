from sys import argv
def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Salary - {time * rate + bonus}")
    except ValueError:
        print("Введите три числа. Не строки и не пустой ввод")

salary()