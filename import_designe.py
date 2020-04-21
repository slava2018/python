#! /usr/bin/env python
# -*- coding: utf-8 -*-

# pip install pyside2 - установка pyside2

# Работа в QT Designer
# C:\Users\admin\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\PySide2\designer.exe
# Ctrl+R - Показать превью формы
# pyside2-uic "wiki.ui" > "ui_wiki.py" - связать дизайн .ui файл с python
#

# Компиляция
# pyinstaller -F -w -i icons/wiki.ico wiki.py
# -w (windowed, скрывает консоль)

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2.QtCore import QFile
# импортируем связанный py файл с нашим ui файлом
from design_wiki import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # создадим объект
        self.ui = Ui_MainWindow()
        # инициализируем нашу форму
        self.ui.setupUi(self)

        # Добавим действие при нажати на кнопку
        self.ui.pushButton.clicked.connect(self.pushed_button)

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
