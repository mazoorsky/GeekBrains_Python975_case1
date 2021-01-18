def fact(n):
    start_number = 1
    if n == 0:
        yield f"{n}! = 1"
    for i in range(1, n + 1):
        start_number *= i
        yield f"{i}! = {start_number}"

for el in fact(int(input("Введи число для расчета факториала: "))):
    print(el)