from lib import check_input
from random import shuffle, choice
from time import sleep

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
shuffle(cards)

player_points = 0
bot_points = 0
answer = 'да'
move = 1

while answer == 'да':
    # перетаскивает карту в руку
    if move == 1:
        dealer_handler = cards.pop()
        bot_points += dealer_handler
        sleep(2)
        print(f'Компьютеру выпало: {dealer_handler}')

        users_cards = []
        for i in range(2):
            handler = cards.pop()
            users_cards.append(handler)
            player_points += handler
    else:
        handler = cards.pop()
        player_points += handler

    if player_points > 21:
        print(f'Вам выпало: {handler}')
        print('Перебор')
        player_points = 0
        break
    elif player_points == 21:
        print('Black Jack!!!')
        break
    else:
        if move == 1:
            answer = check_input(input(f'''
    =====================
    ОЧКИ:
    Оппонент: {bot_points}
    Вы: {player_points}.
    =====================
    Вам выпало: {users_cards[1]} и {users_cards[0]}.
    Еще?\n
    '''), ['да', 'нет'], True)
        else:
            answer = check_input(input(f'''
    =====================
    ОЧКИ:
    Оппонент: {bot_points}
    Вы: {player_points}.
    =====================
    Вам выпало: {handler}.
    Еще?\n
    '''), ['да', 'нет'], True)

    move += 1

else:
    while bot_points < 18:
        dealer_handler = cards.pop()
        bot_points += dealer_handler
        sleep(2)
        print(f'''
        Компьютеру выпало: {dealer_handler}
        =====================
        ОЧКИ:
        Оппонент: {bot_points}
        Вы: {player_points}.
        =====================
            ''')
        if bot_points > 21:
            print('Перебор')
            bot_points  = 0


if bot_points == player_points:
    print('\nНичья!')
elif bot_points < player_points:
    print('\nТы победил!')
else:
    print('\nКомпьютер победил')