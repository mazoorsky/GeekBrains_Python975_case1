# прогресс бегуна

first_result = int(input("Сколько км пробежал в первый день? "))
last_result = int(input("Сколько км хочешь бегать? "))
day = 1
print("1 день:", first_result)

while first_result <= last_result:
    first_result = first_result + first_result * 0.1
    day += 1
    print(day, "день:", "%.2f" % (first_result))
if first_result > last_result:
    print("Ты пробежишь", last_result, "км на", day, "день")