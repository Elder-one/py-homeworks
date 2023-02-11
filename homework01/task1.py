num = int(input('Введите трёхзначное число --> '))
summa = 0;

if 99 < num < 1000:
    while num > 0:
        summa += num % 10
        num //= 10
    print(summa)

else:
    print('Число должно быть трёхзначным')
