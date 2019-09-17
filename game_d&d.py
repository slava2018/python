# Игра "Подземелья Драконов"
import random,time

def displayIntro():
    print('''
    Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры.
    В одной из них дружелюбный дракон, готовый поделиться с вами золотом, а в другой - враждебный, готовый вас сьесть.
    Попытайтесь выйти из пещеры, унеся как можно больше сокровищ.
    ''')

def chooseCave():
    print('В какую пещеру вы пойдете, левую или правую?')
    choosenCave = input()
    choosenCave = choosenCave.lower()
    return choosenCave

def checkCave(cave):
    friendly = random.randint(1,2)
    if cave == 'левую':
        cave = 1
    if cave == 'правую':
        cave = 2

    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Ее темнота заставляет вас дрожать от страха.')
    time.sleep(2)
    print('Огромный дракон появляется перед вами и...')
    time.sleep(2)

    if cave == friendly:
        print(' делится с вами сокровищами!')
    else:
        print(' моментально вас съедает!')

displayIntro()
play_again = 'да'
while play_again == 'да':
    checkCave(chooseCave())
    print('Сыграть еще? (Да/Нет)')
    play_again = input()
    play_again = play_again.lower()