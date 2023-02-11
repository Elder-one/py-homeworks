total_count = int(input('Введите общее число журавликов --> '))

if total_count % 6 == 0:
    part = total_count // 6
    print(f'Петя - {part}')
    print(f'Сережа - {part}')
    print(f'Катя - {4*part}')

else:
    print('Такое число журавликов не удовлетворяет условию задачи')
