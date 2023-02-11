coins_num = int(input('Введите число монеток на столе --> '))
heads_count = tails_count = 0
for i in range(coins_num):
    curr_coin = int(input(f'Состояние монетки {i+1} --> '))
    if curr_coin == 0:
        heads_count += 1
    elif curr_coin == 1:
        tails_count += 1
    else:
        print('!!! ВНИМАНИЕ !!!\nДанная монетка учитываться не будет')

if heads_count > tails_count:
    print(tails_count)
else:
    print(heads_count)
