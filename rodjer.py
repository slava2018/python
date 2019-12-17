from random import randint, choice
from timeit import default_timer
from os.path import isfile
from os import rename, remove
from lib import *

def error_warnings():

    list = ['Ты ошибся!','Ты ошибся!!','Ты ошибся!!!', 'Ты ошибся!!!!','Ты ошибся!!!!!']
    number = randint(0,len(list)-1)
    print(list[number])

def select_mode(mods = 0):
    if mods == 1:
        mode_var = '\n   3 - работа над ошибками'
    else:
        mode_var = ''
    print(f'''
    Режимы:
   1 - тренировка
   2 - настройки{mode_var}
   0 - выход
    ''')
    mode = input('Выбери режим\n')
    if mods == 1:
        while mode not in {'1', '2', '0'}:
            mode = input('Выбери режим\n')
    else:
        while mode not in {'1', '0'}:
            mode = input('Выбери режим\n')

    return mode

def correct_answer_generation(number1, number2, sign):

    number1 = int(number1)
    number2 = int(number2)


    # Генерирует правильный ответ
    if sign == '+':
        right_answer = number1 + number2
    if sign == '-':
        right_answer = number1 - number2

    return right_answer

def example_generation(maximum_answer):
    maximum_answer = int(maximum_answer)  # Максимально возможное число

    # Первая версия примера
    number1 = randint(1, maximum_answer)
    number2 = randint(1, maximum_answer)
    sign = choice('+-')

    # Проверка соответствия правилам
    while number2 + number1 > maximum_answer:
        number1 = randint(1, maximum_answer)
        number2 = randint(1, maximum_answer)
    if number2 > number1:
        sign = '+'

    example_line =  [number1, number2, sign]
    return example_line

def create_mistakes_file(name, mistake):
    file_name = ('mistakes_' + name + '2.txt')
    if isfile(file_name):
        with open(file_name, 'a') as new_mistakes:
            new_mistakes.write(mistake)
    else:
        with open(file_name, 'w') as new_mistakes:
            new_mistakes.write(mistake)

def yes_or_not(answer):
    while answer not in {'да', 'нет'}:
        print('''Ты ошибся, должно быть 'да' или 'нет'.
    Введи заново.''')
        answer = input()
        answer = answer.lower()
        if answer not in {'да', 'нет'}:
            print('''Ты ошибся, должно быть 'да' или 'нет'.
    Введи заново.''')
            answer = input()
            answer = answer.lower()
        return answer

def choise_digit(answer):
    while not answer.isdigit():
        print('Ты ошибся, введи цифру')
        start = default_timer()  # начало отсчета
        answer = input()
        stop = default_timer()  # конец отсчёта
        if not answer.isdigit():
            print('Ты ошибся, введи цифру')
            start = default_timer()  # начало отсчета
            answer = input()
            stop = default_timer()  # конец отсчёта
        global answers_time
        answers_time += round(stop - start)  # Время ответа

def count():
    examples_quantity = ''  # Количество примеров
    maximum_answer = ''  # Максимальное число
    answers_time = 0  # Время ответов

    print('Давай проверим твои знания в математике.')
    # Продолжается пока пользователь не введет положительное число
    while not examples_quantity.isdigit():
        print(name + ', сколько примеров ты готов решить?')
        examples_quantity = input()
        if examples_quantity.isdigit():
            while int(examples_quantity) < 1:
                print('Введи число больше 0')
                examples_quantity = input()
                choise_digit(examples_quantity)
        else:
            print('Ты ошибся, введи цифру')

    # Продолжается пока пользователь не введет положительное число
    while not maximum_answer.isdigit():
        print('До скольки будем считать? Например до 100.')
        maximum_answer = input()
        if maximum_answer.isdigit():
            while int(maximum_answer) < 2:
                print('Введи число больше 1')
                maximum_answer = input()
                choise_digit(maximum_answer)
        else:
            print('Ты ошибся, введи цифру')

    print('Хорошо, тогда начинаем...')

    fails = 0
    rights = 0
    number_of_repeats = 3

    # Генерирует и выводит пример

    for example_kol in range(int(examples_quantity)):
        print('Пример ' + str(example_kol + 1) + ':')
        example_line = example_generation(maximum_answer)
        number1, number2, sign = example_line
        right_answer = correct_answer_generation(number1, number2, sign)

        example = f'{number1} {sign} {number2}'
        print(f'Сколько будет {example}?')

        start = default_timer()  # начало отсчета
        answer = input()
        stop = default_timer()  # конец отсчёта
        answers_time += round(stop - start)  # Время ответа

        # Продолжается пока пользователь не введет положительное число
        choise_digit(answer)
        answer = int(answer)
        # Считает количество правильных и неправильных ответов
        if answer == right_answer:
            rights += 1
            print('Правильно.')
        else:
            fails += 1
            error_warnings()

            # Создание файла с ошибками

            with open(('mistakes_' + name + '.txt'), 'a') as mistakes:
                mistakes.write(f'{example} {number_of_repeats}\n')

    print('Правильных ответов:' + str(rights))
    print('Ошибок:' + str(fails))
    print('Ты справился за' + seconds_convert(answers_time))


def fix_mistakes():
    answer = 1
    with open(('mistakes_' + name + '.txt'), 'r') as mistakes_file:
        print('Хорошо, начнем.')

        m_example = mistakes_file.readline()
        while answer != 'стоп':
            number1, sign, number2, number_of_repeats = m_example.split()
            right_answer = correct_answer_generation(number1, number2, sign)
            print(number1 + sign + number2)
            answer = input()

            if answer != 'стоп':
                if int(answer) == int(right_answer):
                    print('Правильно! Следующий пример:')
                    number_of_repeats = int(number_of_repeats)
                    number_of_repeats += -1
                    if number_of_repeats != 0:
                        create_mistakes_file(name, f'{number1} {sign} {number2}  {number_of_repeats}\n')
                else:
                    print('Ты ошибся.')
                    # Создает или открывает новый файл с ошибками
                    create_mistakes_file(name, m_example)
                print('Если устал, напиши "стоп".')
                m_example = mistakes_file.readline()
                if m_example == '':
                    print('Ты исправил все свои ошибки!')
                    answer = 'стоп'
        print('Устал? Хорошо, ты можешь продолжить исправлять свои ошибки позже.')
        # Дописывает строчки из прошлого файла в новый
        while  m_example != '':
            create_mistakes_file(name, m_example)
            m_example = mistakes_file.readline()

    # Переименовывает новый файл и удаляет старый
    remove('mistakes_' + name + '.txt')
    rename(('mistakes_' + name + '2.txt'), ('mistakes_' + name + '.txt'))


# Основной блок программы
print('Привет! Меня зовут Роджер. А тебя?')
name = input()
name = name.title()
if isfile('settings_' + name + '.txt'):
    print('Давно не виделись, ' + name)
else:
    print('Приятно познакомиться, ' + name)
    with open ('settings_' + name + '.txt', 'w') as new_user:
    	

while True:
    if isfile('mistakes_' + name + '.txt'):
        mode = select_mode(1)
    else:
        mode = select_mode()

    if mode == '1':
        count()

    if mode == '2':
        fix_mistakes()

    elif mode == '0':
        print('До скорых встреч!')
        if isfile('mistakes_' + name + '.txt'):
            new_file_name = remove_same_lines(('mistakes_' + name + '.txt'))
            remove(('mistakes_' + name + '.txt'))
            rename(new_file_name, ('mistakes_' + name + '.txt'))
        break
    else:
        pass

