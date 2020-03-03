from lib import check_input
from random import shuffle


cards = [i for i in range(6,12)]*4
points = 0
shuffle(cards)
answer = 'да'

while answer == 'да':
    # перетаскивает карту в руку
    handler = cards.pop()
    points += handler
    if points > 21:
        print('Перебор')
        break
    elif points == 21:
        print('***21***')
    else:
        answer = check_input(input(f'''
        Вам выпало: {handler}.
        Очки: {points}.
        Еще? (да/нет)\n
    '''), ['да', 'нет'], True)

