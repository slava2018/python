from lib import check_input
from random import randint,shuffle,choice
from time import sleep
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2.QtCore import Qt
# импортируем связанный py файл с нашим ui файлом
from design_21 import Ui_MainWindow

number_card = 2
money = 50

class Deck(object):

    def get_deck(self):
        deck = []

        for suit in ('пики', 'трефы', 'червы', 'бубны'):
            for card in range(2, 11):
                deck.append(f'{card} {suit}')
            for card in ('король', 'дама', 'валет', 'туз'):
                deck.append(f'{card} {suit}')
        shuffle(deck)
        return deck


class Card:
    def get_card_points(self, card, dealer=False):
        card_name = card.split()

        card_points = {}

        for card in range(2, 11):
            card_points[f'{card}'] = card
        for card in ('король', 'дама', 'валет'):
            card_points[f'{card}'] = 10
        if card_name[0] == 'туз':
            if dealer:
                points = choice([1, 11])
            else:
                self.ui.Tuz_1.setVisible(True)
                self.ui.Tuz_2.setVisible(True)
                self.ui.Tuz_answer.setVisible(True)
                self.ui.Stop.setVisible(False)
                self.ui.Start.setVisible(False)
                points = self.ui.Tuz_1.clicked.connect(self.pushed_button_tuz1)
                points = self.ui.Tuz_2.clicked.connect(self.pushed_button_tuz2)
        else:
            points = card_points[card_name[0]]

        return points


class MainWindow(QMainWindow, Deck, Card):
    def __init__(self):
        super(MainWindow, self).__init__()
        # создадим объект
        self.ui = Ui_MainWindow()
        # инициализируем нашу форму
        self.ui.setupUi(self)

        self.ui.Tuz_1.setVisible(False)
        self.ui.Tuz_2.setVisible(False)
        self.ui.Tuz_answer.setVisible(False)

        # Добавим действие при нажати на кнопку
        self.ui.Start.clicked.connect(self.pushed_button_start)
        self.ui.Stop.clicked.connect(self.pushed_button_stop)
        self.ui.cashEdit.setText('0')

        self.ui.Stop.setVisible(False)
        # соберём списки посадочных мест для карт
        # игрок
        self.ucards_seats = list()
        for i in range(1, 12):
            exec(f'self.ucards_seats.append(self.ui.u_card{i})')
        # крупье
        self.dcards_seats = list()
        for i in range(1, 12):
            exec(f'self.dcards_seats.append(self.ui.d_card{i})')



        self.deck = self.get_deck()
        self.ui.money.setText(f'      Деньги:{money}$')

    def pushed_button_tuz1(self):
        self.ui.Tuz_1.setVisible(False)
        self.ui.Tuz_2.setVisible(False)
        self.ui.Tuz_answer.setVisible(False)
        self.ui.Stop.setVisible(True)
        self.ui.Start.setVisible(True)
        return 1


    def pushed_button_tuz2(self):
        self.ui.Tuz_1.setVisible(False)
        self.ui.Tuz_2.setVisible(False)
        self.ui.Tuz_answer.setVisible(False)
        self.ui.Stop.setVisible(True)
        self.ui.Start.setVisible(True)
        return 11

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



    # Метод при нажатии на кнопку
    def pushed_button_start(self):
        global number_card
        global money

        if self.ui.Start.text() == 'Сдать карты':
            if int(self.ui.cashEdit.text()) > money:
                self.ui.Victory.setText('<img src=\'img/no money.png\' />')
            else:
                self.ui.cashEdit.setVisible(False)
                self.ui.cash.setText(f'     Ставка:{self.ui.cashEdit.text()}')
                self.dealer_points = 0
                self.user_points = 0
                self.ui.Victory.setText('')

                dealer_handler = self.deck.pop()
                self.ui.d_card1.setText(f"<img src='img/deck/63x85/{dealer_handler}.png' />")
                self.ui.d_card2.setText(f"<img src='img/deck/63x85/рубашка2.png' />")
                self.dealer_points += self.get_card_points(dealer_handler, dealer=True)
                self.ui.d_points.setText(str(self.dealer_points))

                for i in range(2):
                    user_handler = self.deck.pop()
                    self.ucards_seats[i].setText(f"<img src='img/deck/63x85/{user_handler}.png' />")
                    self.user_points += self.get_card_points(user_handler)
                self.ui.u_points.setText(str(self.user_points))

                self.ui.Start.setText('Ещё')
                self.ui.Stop.setVisible(True)
        else:
            user_handler = self.deck.pop()
            self.ucards_seats[number_card].setText(f"<img src='img/deck/63x85/{user_handler}.png' />")
            self.user_points += self.get_card_points(user_handler)
            self.ui.u_points.setText(str(self.user_points))
            number_card += 1
            if int(self.ui.u_points.text()) == 21:
                self.ui.Start.setVisible(False)
                self.ui.Stop.setVisible(False)
                self.ui.Victory.setText("<img src='img/blackjack.png' />")
                money += int(self.ui.cashEdit.text())*2
                self.ui.money.setText(f'      Деньги:{money}$')
            elif int(self.ui.u_points.text()) > 21:
                self.ui.Start.setVisible(False)
                self.ui.Stop.setVisible(False)
                self.ui.Victory.setText("<img src='img/lose.png' />")
                money -= int(self.ui.cashEdit.text())
                self.ui.money.setText(f'      Деньги:{money}$')

    def pushed_button_stop(self):
        global money
        self.ui.Start.setVisible(False)
        self.ui.Stop.setVisible(False)
        number_card = 1
        while self.dealer_points < 18:
            dealer_handler = self.deck.pop()
            self.dcards_seats[number_card].setText(f"<img src='img/deck/63x85/{dealer_handler}.png' />")
            self.dealer_points += self.get_card_points(dealer_handler, dealer=True)
            self.ui.d_points.setText(str(self.dealer_points))
            number_card +=1
        if self.dealer_points > 21:
            self.ui.Victory.setText("<img src='img/victory.png' />")
            money += int(self.ui.cashEdit.text())
        else:
            if int(self.ui.u_points.text()) < self.dealer_points:
                self.ui.Victory.setText("<img src='img/lose.png' />")
                money -= int(self.ui.cashEdit.text())
            elif int(self.ui.u_points.text()) > self.dealer_points:
                self.ui.Victory.setText("<img src='img/victory.png' />")
                money += int(self.ui.cashEdit.text())
            else:
                self.ui.Victory.setText("<img src='img/draw.png' />")
            self.ui.money.setText(f'      Деньги:{money}$')




        # dealer_points += dealer_handler.value(True)
        # print(f'Компьютеру выпало: {dealer_handler.show()}')
        #
        # users_cards = []
        # for i in range(2):
        #     handler = Card(cards.pop())
        #     print(f'Вам выпало: {handler.show()}')
        #     users_cards.append(handler.show())
        #     player_points += handler.value()

    # else:
    # handler = Card(cards.pop())
    # print(f'Вам выпало: {handler.show()}')
    # player_points += handler.value()


if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())


# class My(object):
#     def __init__(self, name):
#         self.card, self.suit = name.split()
#
#
#     def show(self):
#         name = (f'{self.card} {self.suit}')
#         return name
#
#     def value(self, bot = False):
#
#         if self.card == 'туз':
#             if bot:
#                 points = choice([1, 11])
#             else:
#                 points = int(input('1 или 11?\n'))
#         elif self.card in ('король', 'дама', 'валет', 'туз'):
#             points = 10
#         else:
#             points = self.card
#
#         points = int(points)
#         return points





# cash = 50
# repeat = 'да'
#
# while repeat != 'нет':
#
#     cards = get_deck()
#
#     player_points = 0
#     bot_points = 0
#     answer = 'да'
#     move = 1
#
#     kush = input(f'Ваши деньги:{cash}. Делайте ставку\n')
#     while kush.isdigit() == False:
#         print('Введите число')
#         kush = input(f'Ваши деньги:{cash}. Делайте ставку\n')
#     kush = int(kush)
#     if kush > cash:
#         print('У вас нет столько денег')
#     cash = cash - kush
#
#     while answer == 'да':
#         # перетаскивает карту в руку
#         if move == 1:
#             dealer_handler = Card(cards.pop())
#             bot_points += dealer_handler.value(True)
#             sleep(2)
#             print(f'Компьютеру выпало: {dealer_handler.show()}')
#
#             users_cards = []
#             for i in range(2):
#                 handler = Card(cards.pop())
#                 print(f'Вам выпало: {handler.show()}')
#                 users_cards.append(handler.show())
#                 player_points += handler.value()
#         else:
#             handler = Card(cards.pop())
#             print(f'Вам выпало: {handler.show()}')
#             player_points += handler.value()
#
#         if player_points > 21:
#             print(f'Вам выпало: {handler.show()}')
#             print('Перебор')
#             player_points = 0
#             break
#         elif player_points == 21:
#             print('Black Jack!!!')
#             break
#         else:
#             if move == 1:
#                 answer = check_input(input(f'''
#         =====================
#         ОЧКИ:
#         Оппонент: {bot_points}
#         Вы: {player_points}.
#         =====================
#         Вам выпало: {users_cards[1]} и {users_cards[0]}.
#         Еще?\n
#         '''), ['да', 'нет'], True)
#             else:
#                 answer = check_input(input(f'''
#         =====================
#         ОЧКИ:
#         Оппонент: {bot_points}
#         Вы: {player_points}.
#         =====================
#         Вам выпало: {handler.show()}.
#         Еще?\n
#         '''), ['да', 'нет'], True)
#
#         move += 1
#
#     else:
#         while bot_points < 18:
#             dealer_handler = Card(cards.pop())
#             bot_points += dealer_handler.value(True)
#             sleep(2)
#             print(f'''
#             Компьютеру выпало: {dealer_handler.show()}
#             =====================
#             ОЧКИ:
#             Оппонент: {bot_points}
#             Вы: {player_points}.
#             =====================
#                 ''')
#         if bot_points > 21:
#             print('Перебор')
#             bot_points = 0
#
#     if bot_points == player_points:
#         print('\nНичья!')
#     elif bot_points < player_points:
#         print('\nТы победил!')
#         print(f'Ставка {kush} сыграла')
#         cash += kush * 2
#     else:
#         print('\nКомпьютер победил')
#         print(f'Вы потеряли:{kush}')
#
#     repeat = input('Хотите ли сыграть еще раз?\n')
