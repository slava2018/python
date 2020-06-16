from lib import check_input
from random import randint,shuffle,choice
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2.QtCore import Qt, QTimer, QPropertyAnimation, QRect, QThread
# импортируем связанный py файл с нашим ui файлом
from design_21 import Ui_MainWindow
from threading import Thread
from playsound import playsound

# pyside2-uic "21.ui" > "design_21.py"

number_card = 2
money = 50
cash = 0
# .setEnabled(False) блокировка кнопки
# 16062020

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
                self.ui.Stop.setVisible(False)
                self.ui.Start.setVisible(False)
                self.ui.Tuz_1.clicked.connect(self.pushed_button_tuz1)
                self.ui.Tuz_2.clicked.connect(self.pushed_button_tuz2)
                points = 0
        else:
            points = card_points[card_name[0]]

        return points


class MainWindow(QMainWindow, Deck, Card):
    def cashCheck(self):
        doit = ''
        if money < int(self.ui.coin100.text()):
            doit += 'self.ui.coin100.setVisible(False)\n'
        if money < int(self.ui.coin25.text()):
            doit += 'self.ui.coin25.setVisible(False)\n'
        if money < int(self.ui.coin5.text()):
            doit += 'self.ui.coin5.setVisible(False)\n'
        if money < int(self.ui.coin1.text()):
            doit += 'self.ui.coin1.setVisible(False)\n'
        exec(doit)


    def activate_chips(self, enabled):
        chips = ('1', '5', '100', '25')
        for chip in chips:
            exec(f'self.ui.coin{chip}.setEnabled({enabled})')

    def start(self):
        global cash
        # Добавим действие при нажати на кнопку
        self.cashCheck()
        self.ui.Stop.setVisible(False)
        self.ui.Restart.setVisible(False)
        self.ui.Tuz_1.setVisible(False)
        self.ui.Tuz_2.setVisible(False)
        self.ui.Victory.setText('')
        self.activate_chips(True)
        self.ui.rate.setText('')
        self.ui.rate.setVisible(True)
        self.ui.u_points.setText('')
        self.ui.d_points.setText('')
        self.ui.settings.setGeometry(961, 0, 201, 641)
        for player in {'d_card','u_card'}:
            for card in range(1,11):
                exec(f'self.ui.{player}{card}.setText(\'\')')
        self.ui.Start.setVisible(True)
        self.ui.Start.setText('Сдать карты')
        self.ui.Dialog.setVisible(False)
        cash = 0
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
        self.ui.money.setText(f'    Деньги:{money}$')

    def __init__(self):
        super(MainWindow, self).__init__()
        # создадим объект
        self.ui = Ui_MainWindow()
        # инициализируем нашу форму
        self.ui.setupUi(self)
        self.timer = QTimer(self)

        self.play_my_sound('Frank Sinatra - Strangers In The Night.mp3')

        # спрячем заголовок окна
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.start()
        self.ui.Start.clicked.connect(self.pushed_button_start)
        self.ui.Stop.clicked.connect(self.pushed_button_stop)
        self.ui.Restart.clicked.connect(self.start)
        self.ui.close.clicked.connect(self.close)
        self.ui.coin1.clicked.connect(self.pushed_coin_button)
        self.ui.coin5.clicked.connect(self.pushed_coin_button)
        self.ui.coin25.clicked.connect(self.pushed_coin_button)
        self.ui.coin100.clicked.connect(self.pushed_coin_button)
        self.ui.Reset.clicked.connect(self.pushed_reset)

    def pushed_show_settings(self):
        #from PySide2.QtCore import QPropertyAnimation, QRect
        self.anim = QPropertyAnimation(self.ui.settings, b"geometry")
        self.anim.setDuration(1000) #Длительность
        self.anim.setStartValue(QRect(961, 0, 201, 641)) #Стартовые значения (за границей)
        self.anim.setEndValue(QRect(760, 0, 201, 641)) #Конечные значения
        self.anim.start()

    def pushed_reset(self):
        global cash
        self.ui.rate.setText(str(cash))
        cash = 0

    def play_my_sound(self, sound):
        s = Thread(target=playsound, args=[f'sounds/{sound}'], kwargs={'block':False}, name='music')
        s.start()

    def pushed_coin_button(self):
        global cash,money
        button = self.sender()
        cash += int(button.text())
        self.ui.rate.setText(str(cash))
        self.cashCheck()

    def pushed_button_tuz1(self):
        self.ui.Tuz_1.setVisible(False)
        self.ui.Tuz_2.setVisible(False)
        self.ui.Stop.setVisible(True)
        self.ui.Start.setVisible(True)
        self.user_points += 1
        self.ui.u_points.setText(str(self.user_points))

    def autotuz(self,bot):
        if bot | self.ui.Avtotuz.isChecked(True):
            if int(self.ui.d_points.text()) > 10:
                point = 1
            else:
                point = 11


    def pushed_button_tuz2(self):
        self.ui.Tuz_1.setVisible(False)
        self.ui.Tuz_2.setVisible(False)
        self.ui.Stop.setVisible(True)
        self.ui.Start.setVisible(True)
        self.user_points += 11
        self.ui.u_points.setText(str(self.user_points))

    def keyPressEvent(self, event):
        key = event.key()
        # клавишу Enter
        if key == Qt.Key_Enter:
            pass
        # клавишу ESC
        elif key == Qt.Key_Escape:
            self.close()
        else:
            self.pushed_button()
            super().keyPressEvent(event)

    def cardAnim(self, card, card_img):
        #card = self.ui...
        def start():
            self.anim.start()
        card.setText(f"<img src='img/deck/63x85/{card_img}.png' />")

        self.anim = QPropertyAnimation(card, b"geometry")
        self.anim.setDuration(500)  # Длительность
        self.anim.setStartValue(self.ui.deck.geometry())  # Стартовые значения (за границей)
        self.anim.setEndValue(card.geometry())  # Конечные значения
        QTimer.singleShot(200, start)


    # Метод при нажатии на кнопку
    def pushed_button_start(self):
        global number_card
        global money
        global cash

        if self.ui.Start.text() == 'Сдать карты':
            if self.ui.rate.text().isdigit():
                if int(self.ui.rate.text()) > money:
                    self.ui.Dialog.setVisible(True)
                    self.ui.Dialog.setText(' У вас недостаточно денег!')
                else:
                    self.activate_chips(False)
                    self.ui.rate.setVisible(False)
                    self.ui.cash.setText(f'     Ставка:{self.ui.rate.text()}')
                    self.dealer_points = 0
                    self.user_points = 0
                    self.ui.Victory.setText('')

                    dealer_handler = self.deck.pop()
                    QTimer.singleShot(1000, lambda: self.cardAnim(self.ui.d_card1, dealer_handler))
                    QTimer.singleShot(2000, lambda: self.cardAnim(self.ui.d_card2, 'рубашка2'))
                    self.dealer_points += self.get_card_points(dealer_handler, dealer=True)
                    self.ui.d_points.setText(str(self.dealer_points))

                    for i in range(2):
                        user_handler = self.deck.pop()
                        QTimer.singleShot(1000, lambda: self.cardAnim(self.ucards_seats[i], user_handler))
                        self.user_points += self.get_card_points(user_handler)

                    self.ui.u_points.setText(str(self.user_points))

                    self.ui.Start.setText('Ещё')
                    self.ui.Stop.setVisible(True)
            else:
                self.ui.Dialog.setVisible(True)
                self.ui.Dialog.setText('  Сделайте вашу ставку!')
        else:
            user_handler = self.deck.pop()
            QTimer.singleShot(1000, lambda: self.cardAnim(self.ucards_seats[number_card], user_handler))
            self.user_points += self.get_card_points(user_handler)
            self.ui.u_points.setText(str(self.user_points))
            number_card += 1
            if int(self.ui.u_points.text()) == 21:
                self.ui.Start.setVisible(False)
                self.ui.Stop.setVisible(False)
                self.ui.Victory.setText("<img src='img/blackjack.png' />")
                money += int(self.ui.rate.text())*2
                self.ui.money.setText(f'      Деньги:{money}$')
                self.ui.Restart.setVisible(True)
            elif int(self.ui.u_points.text()) > 21:
                self.ui.Start.setVisible(False)
                self.ui.Stop.setVisible(False)
                self.ui.Victory.setText("<img src='img/lose.png' />")
                money -= int(self.ui.rate.text())
                self.ui.money.setText(f'      Деньги:{money}$')
                self.ui.Restart.setVisible(True)

    def pushed_button_stop(self):
        global money
        self.ui.Start.setVisible(False)
        self.ui.Stop.setVisible(False)
        number_card = 1
        while self.dealer_points < 18:
            dealer_handler = self.deck.pop()
            QTimer.singleShot(1000, lambda: self.cardAnim(self.dcards_seats[number_card], dealer_handler))
            self.dealer_points += self.get_card_points(dealer_handler, dealer=True)
            self.ui.d_points.setText(str(self.dealer_points))
            number_card +=1
        if self.dealer_points > 21:
            self.ui.Victory.setText("<img src='img/victory.png' />")
            money += int(self.ui.rate.text())
            self.ui.money.setText(f'      Деньги:{money}$')
            self.ui.Restart.setVisible(True)
        else:
            if int(self.ui.u_points.text()) < self.dealer_points:
                self.ui.Victory.setText("<img src='img/lose.png' />")
                money -= int(self.ui.rate.text())
                self.ui.money.setText(f'      Деньги:{money}$')
                self.ui.Restart.setVisible(True)
            elif int(self.ui.u_points.text()) > self.dealer_points:
                self.ui.Victory.setText("<img src='img/victory.png' />")
                money += int(self.ui.rate.text())
                self.ui.money.setText(f'      Деньги:{money}$')
                self.ui.Restart.setVisible(True)
            else:
                self.ui.Victory.setText("<img src='img/draw.png' />")
                self.ui.money.setText(f'      Деньги:{money}$')
                self.ui.Restart.setVisible(True)


if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())
