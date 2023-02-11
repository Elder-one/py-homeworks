sum_ = int(input('Введите сумму двух натуральных чисел <= 1000 --> '))
prod = int(input('Введите произведение тех же натуральных чисел <= 1000 --> '))

if 1000+1000 >= sum_ >= 1+1 and 1000*1000 >= prod >=1*1:

    running = True
    for i in range(1, 1000 + 1):
        if not running:
            break
        for j in range(1, 1000 + 1):
            if i*j == prod and i+j == sum_:
                print(f'{i} {j}')
                running = False
                break
    if running:
        print('Таких натуральных чисел не существует')

else:
    print('Введённые параметры не соответствуют условию')
