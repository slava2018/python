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
"}")
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
        self.u_card1.setGeometry(QRect(30, 20, 63, 85))
        self.u_card1.setPixmap(QPixmap(u"img/deck/63x85/\u043a\u043e\u0440\u043e\u043b\u044c \u0447\u0435\u0440\u0432\u044b.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 960, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

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
    # retranslateUi

