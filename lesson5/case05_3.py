with open('employees.txt', 'r', encoding='utf-8') as f:
    employees = {}
    salary_sum = 0
    for line in f:
        print(line.replace('\n', ''))
        key, value = line.split()
        employees[key] = value
        salary_sum = salary_sum + int(value)
        if int(value) < 20000:
            print(f'{key}: зарплата меньше 20000')
    print(f'Личный состав администрации Тупичака: {len(employees[key])} человек')
    print(f'Средняя зарплата в Тупичке: {salary_sum / (len(employees[key]))} рублей')
