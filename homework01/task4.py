width = int(input('ширина --> '))
length = int(input('длина --> '))
count = int(input('Сколько хотите отломать --> '))

if (count < width*length) and ((count % width == 0) or (count % length == 0)):
    print('Yes')
else:
    print('No')
