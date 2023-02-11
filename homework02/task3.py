num = int(input('Введите целое число N --> '))
if num > 0:
    curr_pow = 1
    while curr_pow <= num:
        print(curr_pow)
        curr_pow *= 2

else:
    print('Не существует целых неотрицательных степеней двойки, не превосходящих данное число')
    
