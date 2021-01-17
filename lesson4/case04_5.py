from functools import reduce

def start_list(el_1, el_2):
    return el_1 * el_2

new_list = [el for el in range(100, 1001, 2)]
print(reduce(start_list, new_list))