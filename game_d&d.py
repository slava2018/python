# Игра "Подземелья Драконов"
import random,time

def displayIntro():
    print('''
    Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры.
    В одной из них дружелюбный дракон, готовый поделиться с вами золотом, а в другой - враждебный, готовый вас сьесть.
    Попытайтесь выйти из пещеры, унеся как можно больше сокровищ.
    ''')
    global hp
    global cash
    cash = 0
    hp = 3

def chooseCave():
    print('В какую пещеру вы пойдете, левую или правую?')
    choosenCave = input()
    choosenCave = choosenCave.lower()
    return choosenCave

def checkCave(cave):
    global hp
    global cash

    random_enemy = random.randint(1,3)
    friendly = random.randint(1,2)
    if cave == 'левую':
        cave = 1
    if cave == 'правую':
        cave = 2

    print('Вы приближаетесь к пещере...')
    time.sleep(1)
    print('Ее темнота заставляет вас дрожать от страха.')
    time.sleep(1)
    print('Огромный дракон появляется перед вами и...')
    time.sleep(1)

    if cave == friendly:
        print(' делится с вами сокровищами!')
        cash = cash + 1
    else:
        if random_enemy == 1:
            hp = hp - 1
            print(' ударяет вас хвостом с такой силой, что вас отбрасывает к стене.')
            if hp > 0:
                print(' Кряхтя от боли вы выбираетесь из пещеры.')
        if random_enemy == 2:
            hp = hp - 3
            print(' бросается на вас так стремительно, что вы не успеваете ничего сделать!')
        if random_enemy == 3:
            text = '.'
            if cash>0:
                cash = cash-1
                text = (', потеряв одну монету')
            print(' готовится к броску на вас!')
            time.sleep(1)
            print('Вы в панике убегаете' + text)

def Death():
    global cash
    print('Подземелье поглотило вас. Вы погибли')
    cash = str(cash)
    print('Вы нашли целых ' + cash + ' золотых монет! Сыграть еще? (Да/Нет)')
    play_again = input()
    play_again = play_again.lower()




play_again = 'да'
while play_again == 'да':
    displayIntro()
    while hp>0:
        checkCave(chooseCave())
    Death()