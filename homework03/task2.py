price_dict = {
    'AEIOULNSTR': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10,
    'АВЕИНОРСТ': 1,
    'ДКЛМПУ': 2,
    'БГЁЬЯ': 3,
    'ЙЫ': 4,
    'ЖЗХЦЧ': 5,
    'ШЭЮ': 8,
    'ФЩЪ': 10
    }


word = input('Введите слово на русской или английской раскладке --> ')
points = 0

for ch in word:
    for key, value in price_dict.items():
        if ch.capitalize() in key:
            points += value
            break

print(f'Ваше слово оценивается в {points} очков')
