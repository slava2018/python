# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
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
        MainWindow.resize(742, 581)
        icon = QIcon()
        icon.addFile(u"icons/wiki1.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow\n"
"{\n"
"	background-image:url(img/lib.jpg);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 181, 51))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 70, 591, 41))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(610, 70, 121, 41))
        self.pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: #aa5500;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"	font: 63 12pt \"Open Sans Semibold\";\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #bb5500;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/wiki.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(32, 32))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 120, 721, 461))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u042d\u043d\u0446\u0438\u043a\u043b\u043e\u043f\u0435\u0434\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u0418\u0421\u041a \u0412 \u042d\u041d\u0426\u0418\u041a\u041b\u041e\u041f\u0415\u0414\u0418\u0418:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
    # retranslateUi

