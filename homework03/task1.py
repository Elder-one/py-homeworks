from random import randint

list_size = int(input('Введите размер списка --> '))
list_ = [randint(1, 100) for _ in range(list_size)]

print(list_)
my_number = int(input('Введите искомое число --> '))

nearest = list_[0]
count = 1 if nearest == my_number else 0

for i in range(1, list_size):
    diff = abs(list_[i] - my_number)
    if diff == 0:
        count += 1
    elif diff < abs(nearest - my_number):
        nearest = list_[i]


if count > 0:
    print(f'Найдено {count} таких чисел')
else:
    print(f'Ближайшее к искомому = {nearest}')
