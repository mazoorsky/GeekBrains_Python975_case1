from itertools import count
from itertools import cycle

my_list = []
for el in count(15):
    if el > 23:
        break
    else:
        my_list.append(el)

print(my_list)

i = 0
cyc_list = [4, 8, 15, 16]
for el in cycle(cyc_list):
    if i > 14:
        break
    print(el)
    i += 1