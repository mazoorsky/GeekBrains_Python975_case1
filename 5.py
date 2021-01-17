# рентабельность бизнеса

income = int(input("Каков размер прибыли? "))
costs = int(input("Каков размер издержек? "))
marge = income / costs * 100

if income < costs:
    print("Вы работаете в минус :(")
elif income > costs:
    print("Вы работаете в плюс! Чистая прибыль составила", "%.2f" % marge, "процентов от вложений.")
    employees = int(input("Сколько сотрудников в фирме? "))
    print("На каждого сотрудника приходится по", (income - costs) / employees , "денег.")
else:
    print("Приход равен расходу. Вы работаете в ноль :/")