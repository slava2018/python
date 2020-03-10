from lib import check_input
from random import shuffle, choice
from time import sleep


cards = [i for i in range(6,12)]*4
shuffle(cards)

player_points = 0
player_cards = 0
answer = 'да'

print('\nХод игрока\n')

while answer == 'да':
    # перетаскивает карту в руку
    handler = cards.pop()
    player_cards +=1
    player_points += handler
    if player_points > 21:
        print('Перебор')
        player_points = 0
        break
    elif player_points == 21:
        print('21!')
        break
    else:
        answer = check_input(input(f'''
    Вам выпало: {handler}.
    Очки: {player_points}.
    Еще?\n
    '''), ['да', 'нет'], True)

if player_points == 0:
    print(f'Человек перебрал')
else:
    print(f'Очки человека: {player_points}')

print('\nХод компьютера\n')

bot_points = 0
answer = 'да'
while answer == 'да':
    # перетаскивает карту в руку
    handler = cards.pop()
    bot_points += handler
    if bot_points > 21:
        print('Перебор')
        bot_points = 0
        break
    elif bot_points == 21:
        print('21!')
        break
    else:
        print('Еще?')
        sleep(2)
        if player_cards > 3:
            answer = 'нет'
        elif bot_points > 16:
            answer = 'нет'
        elif bot_points > 10:
            answer = choice('да','нет')
        else:
            answer = 'да'
    print(answer)

if bot_points == 0:
    print(f'Компьютер перебрал')
else:
    print(f'Очки компьютера: {bot_points}\n')

if bot_points == player_points:
    print('\nНичья!')
elif bot_points < player_points:
    print('\nЧеловек победил!')
else:
    print('\nКомпьютер победил')
