from lib import check_input
from random import randint,shuffle,choice
from time import sleep
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2.QtCore import Qt
# импортируем связанный py файл с нашим ui файлом
from design_21 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # создадим объект
        self.ui = Ui_MainWindow()
        # инициализируем нашу форму
        self.ui.setupUi(self)

        # Добавим действие при нажати на кнопку
        #self.ui.pushButton.clicked.connect(self.pushed_button)

    def keyPressEvent(self, event):
        key = event.key()
        # клавишу Enter
        if key == Qt.Key_Enter:
            pass
            # установить через QT Designer focus policy в значение strong focus для нужной Qsearch_button
        # клавишу ESC
        elif key == Qt.Key_Escape:
            self.close()
        else:
            self.pushed_button()
            super().keyPressEvent(event)

    # функция при нажатии на кнопку
    def pushed_button(self):
        # добавим текст в строку
        # self.ui.lineEdit.setText('ok')
        # получим текст с строки поиска
        text = search = self.ui.lineEdit.text()
        # выведем контент в текстовый браузер
        self.ui.textBrowser.setText(text)


if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())


class My(object):
    def __init__(self, name):
        self.card, self.suit = name.split()


    def show(self):
        name = (f'{self.card} {self.suit}')
        return name

    def value(self, bot = False):

        if self.card == 'туз':
            if bot:
                points = choice([1, 11])
            else:
                points = int(input('1 или 11?\n'))
        elif self.card in ('король', 'дама', 'валет', 'туз'):
            points = 10
        else:
            points = self.card

        points = int(points)
        return points


class Card(My):
    def ok(self):
        print('ok')
    def __init__(self, name):
        self.ok()
        super().__init__(name)


def get_deck():
    deck = []

    for suit in ('пики', 'крести', 'черви', 'бубны'):
        for card in range(2, 11):
            deck.append(f'{card} {suit}')
        for card in ('король', 'дама', 'валет', 'туз'):
            deck.append(f'{card} {suit}')
    shuffle(deck)
    return deck


#def get_card_points(card, bot = False):
    #card_name = card.split()
    
    #card_points = {}
    
    #for card in range(2,11):
        #card_points[f'{card}'] = card
    #for card in ('король', 'дама', 'валет'):
        #card_points[f'{card}'] = 10
    #if card_name[0] == 'туз':
        #if bot:
            #points = choice([1, 11])
        #else:
            #points = int(input('1 или 11?\n'))
    #else:
        #points = card_points[card_name[0]]

    #return points

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
            dealer_handler = Card(cards.pop())
            bot_points += dealer_handler.value(True)
            sleep(2)
            print(f'Компьютеру выпало: {dealer_handler.show()}')

            users_cards = []
            for i in range(2):
                handler = Card(cards.pop())
                print(f'Вам выпало: {handler.show()}')
                users_cards.append(handler.show())
                player_points += handler.value()
        else:
            handler = Card(cards.pop())
            print(f'Вам выпало: {handler.show()}')
            player_points += handler.value()

        if player_points > 21:
            print(f'Вам выпало: {handler.show()}')
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
        Вам выпало: {handler.show()}.
        Еще?\n
        '''), ['да', 'нет'], True)

        move += 1

    else:
        while bot_points < 18:
            dealer_handler = Card(cards.pop())
            bot_points += dealer_handler.value(True)
            sleep(2)
            print(f'''
            Компьютеру выпало: {dealer_handler.show()}
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
