from lib import check_input
from random import randint,shuffle,choice
from time import sleep
from  pprint import pprint


class Card(object):
    def __init__(self, suit, card):
        self.suit = suit
        self.card = card
    def show(self):
        print(self.card, self.suit)

i = Card('пики', '5')
i.show()

def get_deck():
    deck = []

    for suit in ('пики', 'крести', 'черви', 'бубны'):
        for card in range(2, 11):
            deck.append(f'{card} {suit}')
        for card in ('король', 'дама', 'валет', 'туз'):
            deck.append(f'{card} {suit}')
    shuffle(deck)
    return deck

def get_card_points(card, bot = False):
    card_name = card.split()
    
    card_points = {}
    
    for card in range(2,11):
        card_points[f'{card}'] = card
    for card in ('король', 'дама', 'валет'):
        card_points[f'{card}'] = 10
    if card_name[0] == 'туз':
        if bot:
            points = choice([1, 11])
        else:
            points = int(input('1 или 11?\n'))
    else:
        points = card_points[card_name[0]]

    return points

cash = 50
repeat = 'да'

while repeat != 'нет':

    cards = get_deck()

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
            bot_points += get_card_points(dealer_handler,True)
            sleep(2)
            print(f'Компьютеру выпало: {dealer_handler}')

            users_cards = []
            for i in range(2):
                handler = cards.pop()
                print(f'Вам выпало: {handler}')
                users_cards.append(handler)
                player_points += get_card_points(handler)
        else:
            handler = cards.pop()
            print(f'Вам выпало: {handler}')
            player_points += get_card_points(handler)

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
            bot_points += get_card_points(dealer_handler, True)
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
