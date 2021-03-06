import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtCore import Qt
from PySide2.QtCore import QFile
# импортируем связанный py файл с нашим ui файлом
from design_wiki import Ui_MainWindow
import wikipedia
from requests import get
from random import randint
from lib import download_files
from os import mkdir, remove
from os.path import exists

wikipedia.set_lang("ru")


class MainWindow(QMainWindow, QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        # создадим объект
        self.ui = Ui_MainWindow()
        # инициализируем нашу форму
        self.ui.setupUi(self)

        # Добавим действие при нажати на кнопку
        self.ui.pushButton.clicked.connect(self.search_in_wiki)

    # метод нажатия клавиш клавиатуры
    # переопределим родительский метод
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
            self.search_in_wiki()
            super().keyPressEvent(event)

    # метод завершения работы
    # переопределим родительский метод
    def closeEvent(self, event):
        if exists(window.image_file_name):
            remove(window.image_file_name)

    # функция при нажатии на кнопку
    def search_in_wiki(self):
        # получим текст с строки поиска
        search = self.ui.lineEdit.text()
        if search == '':
            self.ui.textBrowser.setText('Введите что-то в строку поиска!')
        else:
            try:

                s = wikipedia.page(search)
                # получим путь к картинке и скачаем её

                image_url = s.images[0]
                image = get(image_url)
                with open('img/test.jpg', "wb") as f:
                    f.write(image.content)
                image_source= f"<img src='img/test.jpg' width='300'>"
                self.ui.textBrowser.setText(image_source)
                self.ui.textBrowser.append(s.content)

            except:
                text = (f'''
Возможные варианты:
===================''')
                variants = wikipedia.search(search)
                for item in variants:
                    text += (f'\n{item}')
                text += ('\n===================')
                if text == ('''
Возможные варианты:
===================
==================='''):
                    self.ui.textBrowser.setText('По вашему запросу ничего не найдено.')
                else:
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








# import wikipedia
# wikipedia.set_lang("ru")
#
# while True:
#     try:
#         search = input("Что искать?\n")
#         s = wikipedia.page(search)
#         print(s.content)
#     except:
#         print()
#         print('Возможные варианты:')
#         print('===================')
#         variants = wikipedia.search(search)
#         for item in variants:
#             print(item)
#         print('===================')
