# ввод числа n, вывод суммы n + nn + nnn

n1 = int(input("Введи число: "))

n2 = int("%s%s" % (n1, n1))
n3 = int("%s%s%s" % (n1, n1, n1))

print(n1 + n2 + n3)