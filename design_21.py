# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '21.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 640)
        MainWindow.setMinimumSize(QSize(960, 640))
        MainWindow.setMaximumSize(QSize(960, 640))
        icon = QIcon()
        icon.addFile(u"img/21.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow\n"
"{\n"
"	background: url(\"img/background.jpg\");\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	text-align:right;\n"
"}\n"
"\n"
"QPushButton:selected\n"
"{\n"
"	outline: none;\n"
"}\n"
"\n"
"QPushButton:active\n"
"{\n"
"	outline: none;\n"
"}\n"
"")
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dealer = QLabel(self.centralwidget)
        self.dealer.setObjectName(u"dealer")
        self.dealer.setGeometry(QRect(-40, 420, 201, 221))
        self.dealer.setPixmap(QPixmap(u"img/dealer.png"))
        self.dealer.setScaledContents(True)
        self.d_card1 = QLabel(self.centralwidget)
        self.d_card1.setObjectName(u"d_card1")
        self.d_card1.setGeometry(QRect(160, 530, 63, 85))
        self.d_card2 = QLabel(self.centralwidget)
        self.d_card2.setObjectName(u"d_card2")
        self.d_card2.setGeometry(QRect(190, 530, 63, 85))
        self.d_card3 = QLabel(self.centralwidget)
        self.d_card3.setObjectName(u"d_card3")
        self.d_card3.setGeometry(QRect(220, 530, 63, 85))
        self.d_card4 = QLabel(self.centralwidget)
        self.d_card4.setObjectName(u"d_card4")
        self.d_card4.setGeometry(QRect(250, 530, 63, 85))
        self.d_card5 = QLabel(self.centralwidget)
        self.d_card5.setObjectName(u"d_card5")
        self.d_card5.setGeometry(QRect(280, 530, 63, 85))
        self.d_card6 = QLabel(self.centralwidget)
        self.d_card6.setObjectName(u"d_card6")
        self.d_card6.setGeometry(QRect(310, 530, 63, 85))
        self.d_card7 = QLabel(self.centralwidget)
        self.d_card7.setObjectName(u"d_card7")
        self.d_card7.setGeometry(QRect(340, 530, 63, 85))
        self.d_card8 = QLabel(self.centralwidget)
        self.d_card8.setObjectName(u"d_card8")
        self.d_card8.setGeometry(QRect(370, 530, 63, 85))
        self.d_card9 = QLabel(self.centralwidget)
        self.d_card9.setObjectName(u"d_card9")
        self.d_card9.setGeometry(QRect(400, 530, 63, 85))
        self.d_card10 = QLabel(self.centralwidget)
        self.d_card10.setObjectName(u"d_card10")
        self.d_card10.setGeometry(QRect(430, 530, 63, 85))
        self.d_card11 = QLabel(self.centralwidget)
        self.d_card11.setObjectName(u"d_card11")
        self.d_card11.setGeometry(QRect(460, 530, 63, 85))
        self.u_card1 = QLabel(self.centralwidget)
        self.u_card1.setObjectName(u"u_card1")
        self.u_card1.setGeometry(QRect(60, 50, 63, 85))
        self.u_card2 = QLabel(self.centralwidget)
        self.u_card2.setObjectName(u"u_card2")
        self.u_card2.setGeometry(QRect(90, 50, 63, 85))
        self.u_card3 = QLabel(self.centralwidget)
        self.u_card3.setObjectName(u"u_card3")
        self.u_card3.setGeometry(QRect(120, 50, 63, 85))
        self.u_card4 = QLabel(self.centralwidget)
        self.u_card4.setObjectName(u"u_card4")
        self.u_card4.setGeometry(QRect(150, 50, 63, 85))
        self.u_card5 = QLabel(self.centralwidget)
        self.u_card5.setObjectName(u"u_card5")
        self.u_card5.setGeometry(QRect(180, 50, 63, 85))
        self.u_card6 = QLabel(self.centralwidget)
        self.u_card6.setObjectName(u"u_card6")
        self.u_card6.setGeometry(QRect(210, 50, 63, 85))
        self.u_card7 = QLabel(self.centralwidget)
        self.u_card7.setObjectName(u"u_card7")
        self.u_card7.setGeometry(QRect(240, 50, 63, 85))
        self.u_card8 = QLabel(self.centralwidget)
        self.u_card8.setObjectName(u"u_card8")
        self.u_card8.setGeometry(QRect(270, 50, 63, 85))
        self.u_card9 = QLabel(self.centralwidget)
        self.u_card9.setObjectName(u"u_card9")
        self.u_card9.setGeometry(QRect(300, 50, 63, 85))
        self.u_card10 = QLabel(self.centralwidget)
        self.u_card10.setObjectName(u"u_card10")
        self.u_card10.setGeometry(QRect(330, 50, 63, 85))
        self.u_card11 = QLabel(self.centralwidget)
        self.u_card11.setObjectName(u"u_card11")
        self.u_card11.setGeometry(QRect(360, 50, 63, 85))
        self.Start = QPushButton(self.centralwidget)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(820, 480, 141, 31))
        self.Start.setLayoutDirection(Qt.LeftToRight)
        self.Start.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: url(\"img/more.png\");\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border: none;\n"
"	margin-left: 30px\n"
"}")
        self.Stop = QPushButton(self.centralwidget)
        self.Stop.setObjectName(u"Stop")
        self.Stop.setGeometry(QRect(820, 510, 141, 31))
        self.Stop.setLayoutDirection(Qt.LeftToRight)
        self.Stop.setStyleSheet(u"QPushButton\n"
"{\n"
"	background: url(\"img/stop.png\");\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border: none;\n"
"	margin-left: 30px\n"
"}")
        self.Stop.setCheckable(False)
        self.money = QTextBrowser(self.centralwidget)
        self.money.setObjectName(u"money")
        self.money.setGeometry(QRect(760, 0, 201, 41))
        font = QFont()
        font.setFamily(u"Segoe Print")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.money.setFont(font)
        self.money.setLayoutDirection(Qt.LeftToRight)
        self.money.setStyleSheet(u"QTextBrowser\n"
"{\n"
"	background: url(\"img/money.png\");\n"
"	color:#000000;\n"
"	border: none;\n"
"}")
        self.d_points = QLabel(self.centralwidget)
        self.d_points.setObjectName(u"d_points")
        self.d_points.setGeometry(QRect(160, 490, 81, 21))
        self.d_points.setStyleSheet(u"color: #ffffff;")
        self.u_points = QLabel(self.centralwidget)
        self.u_points.setObjectName(u"u_points")
        self.u_points.setGeometry(QRect(60, 20, 81, 21))
        self.u_points.setStyleSheet(u"color: #ffffff;")
        self.Victory = QLabel(self.centralwidget)
        self.Victory.setObjectName(u"Victory")
        self.Victory.setGeometry(QRect(340, 180, 301, 211))
        self.Tuz_1 = QPushButton(self.centralwidget)
        self.Tuz_1.setObjectName(u"Tuz_1")
        self.Tuz_1.setGeometry(QRect(830, 480, 61, 31))
        font1 = QFont()
        font1.setFamily(u"Sensei Medium")
        font1.setPointSize(16)
        self.Tuz_1.setFont(font1)
        self.Tuz_1.setCursor(QCursor(Qt.ArrowCursor))
        self.Tuz_1.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: #555555;\n"
"	background-color:#cccccc;\n"
"	text-align: center;\n"
"	border-bottom-left-radius: 30 20;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	color: #000000;\n"
"}\n"
"")
        self.Tuz_2 = QPushButton(self.centralwidget)
        self.Tuz_2.setObjectName(u"Tuz_2")
        self.Tuz_2.setGeometry(QRect(890, 480, 61, 31))
        self.Tuz_2.setFont(font1)
        self.Tuz_2.setCursor(QCursor(Qt.ArrowCursor))
        self.Tuz_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: #cccccc;\n"
"	background-color: #555555;\n"
"	text-align: center;\n"
"	border-bottom-right-radius: 30 20;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	color: #ffffff;\n"
"}\n"
"")
        self.cash = QLabel(self.centralwidget)
        self.cash.setObjectName(u"cash")
        self.cash.setGeometry(QRect(780, 50, 121, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe Print")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.cash.setFont(font2)
        self.cash.setStyleSheet(u"QLabel\n"
"{\n"
"	color:#ffffff;\n"
"	border: none;\n"
"}")
        self.Restart = QPushButton(self.centralwidget)
        self.Restart.setObjectName(u"Restart")
        self.Restart.setGeometry(QRect(390, 410, 181, 51))
        font3 = QFont()
        font3.setFamily(u"Segoe Print")
        font3.setPointSize(14)
        self.Restart.setFont(font3)
        self.Restart.setLayoutDirection(Qt.LeftToRight)
        self.Restart.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: #000000 ;\n"
"	border: none;\n"
"	text-align: center;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border: none;\n"
"	color: #000000;\n"
"	background-color: #ffffff;\n"
"}")
        self.Restart.setCheckable(False)
        self.close = QPushButton(self.centralwidget)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(10, 0, 41, 41))
        self.close.setStyleSheet(u"QPushButton\n"
"{\n"
"	text-align:left;\n"
"	border: none;\n"
"	background-color: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"img/close_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon1)
        self.close.setIconSize(QSize(32, 32))
        self.coin5 = QPushButton(self.centralwidget)
        self.coin5.setObjectName(u"coin5")
        self.coin5.setGeometry(QRect(60, 360, 41, 41))
        self.coin5.setMinimumSize(QSize(41, 41))
        self.coin5.setMaximumSize(QSize(41, 41))
        self.coin5.setSizeIncrement(QSize(41, 41))
        self.coin5.setBaseSize(QSize(41, 41))
        font4 = QFont()
        font4.setPointSize(1)
        self.coin5.setFont(font4)
        self.coin5.setLayoutDirection(Qt.RightToLeft)
        self.coin5.setAutoFillBackground(False)
        self.coin5.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: none;\n"
"	padding: -7;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"img/chips/5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coin5.setIcon(icon2)
        self.coin5.setIconSize(QSize(41, 41))
        self.coin5.setFlat(False)
        self.coin1 = QPushButton(self.centralwidget)
        self.coin1.setObjectName(u"coin1")
        self.coin1.setGeometry(QRect(10, 360, 41, 41))
        self.coin1.setMinimumSize(QSize(41, 41))
        self.coin1.setMaximumSize(QSize(41, 41))
        self.coin1.setSizeIncrement(QSize(41, 41))
        self.coin1.setBaseSize(QSize(41, 41))
        self.coin1.setFont(font4)
        self.coin1.setLayoutDirection(Qt.RightToLeft)
        self.coin1.setAutoFillBackground(False)
        self.coin1.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: none;\n"
"	padding: -7;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"img/chips/1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coin1.setIcon(icon3)
        self.coin1.setIconSize(QSize(41, 41))
        self.coin1.setFlat(False)
        self.coin25 = QPushButton(self.centralwidget)
        self.coin25.setObjectName(u"coin25")
        self.coin25.setGeometry(QRect(110, 360, 41, 41))
        self.coin25.setMinimumSize(QSize(41, 41))
        self.coin25.setMaximumSize(QSize(41, 41))
        self.coin25.setSizeIncrement(QSize(41, 41))
        self.coin25.setBaseSize(QSize(41, 41))
        self.coin25.setFont(font4)
        self.coin25.setLayoutDirection(Qt.RightToLeft)
        self.coin25.setAutoFillBackground(False)
        self.coin25.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: none;\n"
"	padding: -7;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"img/chips/25.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coin25.setIcon(icon4)
        self.coin25.setIconSize(QSize(41, 41))
        self.coin25.setFlat(False)
        self.coin100 = QPushButton(self.centralwidget)
        self.coin100.setObjectName(u"coin100")
        self.coin100.setGeometry(QRect(160, 360, 41, 41))
        self.coin100.setMinimumSize(QSize(41, 41))
        self.coin100.setMaximumSize(QSize(41, 41))
        self.coin100.setSizeIncrement(QSize(41, 41))
        self.coin100.setBaseSize(QSize(41, 41))
        self.coin100.setFont(font4)
        self.coin100.setLayoutDirection(Qt.RightToLeft)
        self.coin100.setAutoFillBackground(False)
        self.coin100.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: none;\n"
"	padding: -7;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"img/chips/100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coin100.setIcon(icon5)
        self.coin100.setIconSize(QSize(41, 41))
        self.coin100.setFlat(False)
        self.rate = QLabel(self.centralwidget)
        self.rate.setObjectName(u"rate")
        self.rate.setGeometry(QRect(900, 50, 47, 31))
        self.rate.setFont(font3)
        self.rate.setStyleSheet(u"QLabel\n"
"{\n"
"	color:#ffffff;\n"
"	border: none;\n"
"}")
        self.Reset = QPushButton(self.centralwidget)
        self.Reset.setObjectName(u"Reset")
        self.Reset.setGeometry(QRect(740, 50, 75, 71))
        self.Reset.setStyleSheet(u"QPushButton\n"
"{\n"
"	outline: none;\n"
"	border: none;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"img/reset_rate1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Reset.setIcon(icon6)
        self.Reset.setIconSize(QSize(64, 64))
        self.settings = QFrame(self.centralwidget)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(961, 0, 201, 641))
        self.settings.setStyleSheet(u"background-color: #ffffff;")
        self.settings.setFrameShape(QFrame.StyledPanel)
        self.settings.setFrameShadow(QFrame.Raised)
        self.Avtotuz = QCheckBox(self.settings)
        self.Avtotuz.setObjectName(u"Avtotuz")
        self.Avtotuz.setGeometry(QRect(20, 10, 161, 41))
        font5 = QFont()
        font5.setFamily(u"Open Sans Light")
        font5.setPointSize(12)
        self.Avtotuz.setFont(font5)
        self.deck = QLabel(self.centralwidget)
        self.deck.setObjectName(u"deck")
        self.deck.setGeometry(QRect(30, 250, 91, 91))
        self.deck.setStyleSheet(u"QLabel\n"
"{\n"
"	background: url(\"img/deck.jpg\");\n"
"}")
        self.Dialog = QLabel(self.centralwidget)
        self.Dialog.setObjectName(u"Dialog")
        self.Dialog.setGeometry(QRect(120, 410, 171, 111))
        font6 = QFont()
        font6.setFamily(u"Sensei Medium")
        font6.setPointSize(9)
        self.Dialog.setFont(font6)
        self.Dialog.setStyleSheet(u"QLabel\n"
"{\n"
"	background: url(\"img/dialog.png\");\n"
"}")
        self.Dialog.setPixmap(QPixmap(u"img/dialog.png"))
        self.Dialog.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Stop.setDefault(False)
        self.Restart.setDefault(False)
        self.coin5.setDefault(False)
        self.coin1.setDefault(False)
        self.coin25.setDefault(False)
        self.coin100.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BlackJack", None))
        self.dealer.setText("")
        self.d_card1.setText("")
        self.d_card2.setText("")
        self.d_card3.setText("")
        self.d_card4.setText("")
        self.d_card5.setText("")
        self.d_card6.setText("")
        self.d_card7.setText("")
        self.d_card8.setText("")
        self.d_card9.setText("")
        self.d_card10.setText("")
        self.d_card11.setText("")
        self.u_card1.setText("")
        self.u_card2.setText("")
        self.u_card3.setText("")
        self.u_card4.setText("")
        self.u_card5.setText("")
        self.u_card6.setText("")
        self.u_card7.setText("")
        self.u_card8.setText("")
        self.u_card9.setText("")
        self.u_card10.setText("")
        self.u_card11.setText("")
        self.Start.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0430\u0442\u044c \u043a\u0430\u0440\u0442\u044b", None))
        self.Stop.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0432\u0430\u0442\u0438\u0442", None))
        self.money.setPlaceholderText(QCoreApplication.translate("MainWindow", u"      \u0414\u0435\u043d\u044c\u0433\u0438:", None))
        self.d_points.setText("")
        self.u_points.setText("")
        self.Victory.setText("")
        self.Tuz_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Tuz_2.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.cash.setText(QCoreApplication.translate("MainWindow", u"     \u0421\u0442\u0430\u0432\u043a\u0430:", None))
        self.Restart.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0437\u0430\u043d\u043e\u0432\u043e", None))
        self.close.setText("")
        self.coin5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.coin5.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.coin1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.coin1.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.coin25.setText(QCoreApplication.translate("MainWindow", u"25", None))
#if QT_CONFIG(shortcut)
        self.coin25.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.coin100.setText(QCoreApplication.translate("MainWindow", u"100", None))
#if QT_CONFIG(shortcut)
        self.coin100.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.rate.setText("")
        self.Reset.setText("")
        self.Avtotuz.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0432\u044b\u0431\u043e\u0440 \u0442\u0443\u0437\u0430", None))
        self.deck.setText("")
        self.Dialog.setText("")
    # retranslateUi

