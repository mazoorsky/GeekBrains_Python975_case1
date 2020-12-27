# перевод секунд во время в формате чч:мм:сс. Два варианта решения

# вариант 1
time = int(input("Введи количество секунд: "))

time_hours = time // 3600
time_mins = (time % 3600) // 60
time_secs = ((time % 3600) % 60) % 60

print("%02i:%02i:%02i" % (time_hours, time_mins, time_secs))

# Вариант 2
import time
seconds = int(input("Давай ещё разок: "))

print(time.strftime('%H:%M:%S', time.gmtime(seconds)))