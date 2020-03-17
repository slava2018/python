from lib import check_input
from random import shuffle, choice
from time import sleep

cash = 50
repeat = 'да'

while repeat != 'нет':

    cards = {'J': 10, 'Q': 10, 'K': 10, 'T': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             '10': 10} * 4
    shuffle(cards)

    player_points = 0
    bot_points = 0
    answer = 'да'
    move = 1

    kush = input(f'Ваши деньги:{cash}. Делайте ставку\n')
    while kush.isdigit() == False:
        print('Введите число')
        kush = input(f'Ваши деньги:{cash}. Делайте ставку\n')
    kush = int(kush)
    if kush > cash:
        print('У вас нет столько денег')
    cash = cash - kush

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
            bot_points = 0

    if bot_points == player_points:
        print('\nНичья!')
    elif bot_points < player_points:
        print('\nТы победил!')
        print(f'Ставка {kush} сыграла')
        cash += kush * 2
    else:
        print('\nКомпьютер победил')
        print(f'Вы потеряли:{kush}')

    repeat = input('Хотите ли сыграть еще раз?\n')
