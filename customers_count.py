def groups_count(n_customers, n_first_id=0):              #Объединили два пункта задания задав по умолчанию первое id равным 0
    groups = {}
    for i in range(n_first_id, n_first_id + n_customers): #Проходим по всем id
        num = i
        sum = 0
        while (num != 0):                                 #Находим сумму цифр числа
            sum = sum + num % 10
            num = num // 10
        if groups.get(sum) != None:                       #Если группа есть в словаре увеличиваем значение
            groups[sum] += 1
        else:
            groups[sum] = 1                               #Если группы нет добавляем необходимый ключ со значением 1
    return groups

customers = int(input('Введите количество покупателей'))
first_id = int(input('Введите id первого покупателя'))
result = sorted(groups_count(customers,first_id).items())
for j in result:
    a = j[0]
    b = j[1]
    print(f'Количество покупателей в группе №{a}: {b} человек')




