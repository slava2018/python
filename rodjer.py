#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
from random import randint, choice
from timeit import default_timer
from os.path import isfile
from os import rename, remove
from lib import *
from subprocess import call
import os


def remove_same_lines(filename):

    uniques = []

    with open(filename, 'r') as old_file, open(f'tmp_{filename}', 'a') as new_file:

        for row in old_file:

            part_of_row = row.split()
            number1, sign, number2, repeat = part_of_row

            example = f'{number1} {sign} {number2}'

            if example not in uniques:
                uniques.append(example)
                new_file.write(f'{example} {repeat}\n')

    file = f'tmp_{filename}'
    return file


def error_warnings():

    list = ['Ты ошибся!', 'Ты ошибся!!', 'Ты ошибся!!!', 'Ты ошибся!!!!', 'Ты ошибся!!!!!']
    number = randint(0, len(list)-1)
    print(list[number])


def select_mode(mods=0):
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
        while mode not in {'1', '2', '3', '0'}:
            mode = input('Выбери режим\n')
    else:
        while mode not in {'1', '2', '0'}:
            mode = input('Выбери режим\n')

    return mode


def settings_change():
    print('''Выбери параметр:
        ========================================================
        1 - количество правильных ответов для исправления ошибки
        2 - показывать правильный ответ при ошибке
        3 - однопользовательский режим
        4 - имя пользователя
        5 - сохранять ошибки
        6 - уникальные примеры 
        ========================================================''')

    mode = input('Выбери режим\n')
    while mode not in {'1', '2', '3', '4', '5', '6', ''}:
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
    if number2 > number1:
        sign = '+'
    if sign == '+':
        while number2 + number1 > maximum_answer:
            number1 = randint(1, maximum_answer)
            number2 = randint(1, maximum_answer)



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
    global answers_time
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
    number_of_repeats = answer_numbers
    uniques = []
    global uniq
    # Генерирует и выводит пример
    if uniq == '1':
        if int(examples_quantity)>int(maximum_answer)**2:
            print('Я не знаю столько уникальных примеров.')
            examples_quantity = int(maximum_answer)**2

    for example_kol in range(int(examples_quantity)):
        example_line = example_generation(maximum_answer)

        if uniq == '1':
            if example_line not in uniques:
                uniques.append(example_line)
            else:
                while example_line in uniques:
                    example_line = example_generation(maximum_answer)
                uniques.append(example_line)

        number1, number2, sign = example_line
        right_answer = correct_answer_generation(number1, number2, sign)

        example = f'{number1} {sign} {number2}'
        print('Пример ' + str(example_kol + 1) + ':')
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
            if show_setting == '1':
                print(right_answer)
            if save_mistakes== '1':
                error_warnings()

            # Создание файла с ошибками

            with open(('mistakes_' + name + name_id + '.txt'), 'a') as mistakes:
                mistakes.write(f'{example} {number_of_repeats}\n')

    print('Правильных ответов:' + str(rights))
    print('Ошибок:' + str(fails))
    print('Ты справился за' + seconds_convert(answers_time))


def fix_mistakes():
    answer = 1
    with open(('mistakes_' + name + name_id + '.txt'), 'r') as mistakes_file:
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
                        create_mistakes_file(name + name_id, f'{number1} {sign} {number2}  {number_of_repeats}\n')
                else:
                    print('Ты ошибся.')
                    # Создает или открывает новый файл с ошибками
                    create_mistakes_file(name + name_id, m_example)
                print('Если устал, напиши "стоп".')
                m_example = mistakes_file.readline()
                if m_example == '':
                    print('Ты исправил все свои ошибки!')
                    answer = 'стоп'
        print('Устал? Хорошо, ты можешь продолжить исправлять свои ошибки позже.')
        # Дописывает строчки из прошлого файла в новый
        while  m_example != '':
            create_mistakes_file(name + name_id, m_example)
            m_example = mistakes_file.readline()

    # Переименовывает новый файл и удаляет старый
    remove('mistakes_' + name + name_id + '.txt')
    rename(('mistakes_' + name + name_id +  '2.txt'), ('mistakes_' + name + name_id + '.txt'))


def hide_file(any_file):
    if os.name == 'nt':
        if os.path.exists(any_file):
            call(['atrib', '+h', any_file])
    else:
        return any_file


# Основной блок программы
if isfile('settings.json'):
    with open('settings.json', 'r',  encoding="utf-8") as all_settings:
        all_new_settings = json.load(all_settings)
        setting = all_new_settings['change_mod']
        name = all_new_settings['name']
        name_id = all_new_settings['name_id']


        if setting != '1':
            print('Привет! Как тебя зовут?')
            name = input()
            name = name.title()
            print('У тебя уже есть свой пароль? если да, то введи его ниже')
            name_id = input()
            if name_id == 'нет':
                print('Приятно познакомиться, ' + name)
                name_id = randint(100, 999)
                name_id = str(name_id)
                name_id = str(name_id)
                while isfile('settings_' + name + name_id + '.json'):
                    name_id = randint(100, 999)
                    name_id = str(name_id)
                print('твой пароль:' + name_id)
            else:
                if isfile('settings_' + name + name_id + '.json'):
                    print('Давно не виделись, ' + name)
                else:
                    print('Ты ошибся')
                    print('Приятно познакомиться, ' + name)
                    name_id = randint(100, 999)
                    name_id = str(name_id)
                    while isfile('settings_' + name + name_id + '.json'):
                        name_id = randint(100, 999)
                        name_id = str(name_id)
                    print('твой пароль:' + str(name_id))
        else:
            with open('settings.json', 'r',  encoding="utf-8") as all_settings:
                all_new_settings = json.load(all_settings)
                name = all_new_settings['name']
                setting = all_new_settings['change_mod']
                name_id = all_new_settings['name_id']
                print('Давно не виделись,' + name)

else:
    print('Привет! Меня зовут Роджер. А тебя?')
    name = input()
    name = name.title()
    print('У тебя уже есть свой пароль? если да, то введи его ниже')
    name_id = input()
    if name_id == 'нет':
        print('Приятно познакомиться, ' + name)
        name_id = randint(100, 999)
        name_id = str(name_id)
        while isfile('settings_' + name + name_id + '.json'):
            name_id = randint(100, 999)
            name_id = str(name_id)
        print('твой пароль:' + name_id)
    else:
        if isfile('settings_' + name + name_id + '.json'):
            print('Давно не виделись, ' + name)
        else:
            print('Ты ошибся')
            print('Приятно познакомиться, ' + name)
            name_id = randint(100,999)
            name_id = str(name_id)
            while isfile('settings_' + name + name_id + '.json'):
                name_id = randint(100, 999)
                name_id = str(name_id)
            print('твой пароль:' + str(name_id))

    with open('settings.json', 'w', encoding="utf-8") as all_settings:
        settings_json = {
            'change_mod': '1',
            'name': name,
            'name_id': name_id}
        json.dump(settings_json, all_settings, ensure_ascii=False)

if isfile('settings_' + name + name_id + '.json'):
    with open('settings_' + name + name_id + '.json', 'r', encoding="utf-8") as settings:
        all_new_settings = json.load(settings)
        answer_numbers = all_new_settings['answer_numbers']
        show_setting = all_new_settings['show_setting']
        change_mod = all_new_settings['change_mod']
        name = all_new_settings['name_user']
        save_mistakes = all_new_settings['save_mistakes']
        uniq = all_new_settings['uniq']
else:
    with open('settings_' + name + name_id + '.json', 'w', encoding="utf-8") as settings:
        new_settings = {
        'answer_numbers':'3',
        'show_setting':'1',
        'change_mod':'1',
        'name_user':name,
        'save_mistakes':'1',
        'uniq':'1'
        }

        json.dump(new_settings, settings, ensure_ascii=False)

    with open('settings_' + name + name_id + '.json', 'r', encoding="utf-8") as settings:
        all_new_settings = json.load(settings)
        answer_numbers = all_new_settings['answer_numbers']
        show_setting = all_new_settings['show_setting']
        change_mod = all_new_settings['change_mod']
        name_user = all_new_settings['name_user']
        save_mistakes = all_new_settings['save_mistakes']
        uniq = all_new_settings['uniq']

while True:
    if isfile('mistakes_' + name + name_id + '.txt'):
        mode = select_mode(1)
    else:
        mode = select_mode()

    if mode == '1':
        count()

    if mode == '2':
        change_setting = settings_change()
        while change_setting != '':
            change_setting = settings_change()

            if change_setting == '1':
                print('Сейчас:' + answer_numbers)
                answer_numbers = input()
                while not answer_numbers.isdigit():
                    print('Введи число')
                    answer_numbers = input()

            if change_setting == '2':
                print('Сейчас:' + show_setting)
                print('''========
                        1 - Да
                        2 - Нет
                        ========''')
                show_setting = input()
                while show_setting not in {'1', '2'}:
                    print('Введи 1 или 2')
                    show_setting = input()

            if change_setting == '3':
                print('Сейчас:' + change_mod)
                print('''========
                        1 - Однопользовательский
                        2 - Многопользовательский
                        ========''')
                change_mod = input()
                while change_mod not in {'1', '2'}:
                    print('Введи 1 или 2')
                    change_mod = input()
                with open('settings.json', 'r', encoding="utf-8") as all_settings:
                    all_new_settings = json.load(all_settings)
                    setting = all_new_settings['change_mod']
                    name = all_new_settings['name']
                    name_id = all_new_settings['name_id']
                with open('settings.json', 'w', encoding="utf-8") as all_settings:
                    settings_json = {
                        'change_mod': '2',
                        'name': name,
                        'name_id': name_id}
                    json.dump(settings_json, all_settings, ensure_ascii=False)

            if change_setting == '4':
                print('Сейчас:' + name_user)
                name_user = input()
                name = name_user

            if change_setting == '5':
                print('Сейчас:' + save_mistakes)
                print('''========
                        1 - Да
                        2 - Нет
                        ========''')
                save_mistakes = input()
                while save_mistakes not in {'1', '2'}:
                    print('Введи 1 или 2')
                    save_mistakes = input()

            if change_setting == '6':
                print('Сейчас:' + uniq)
                print('''========
                        1 - Да
                        2 - Нет
                        ========''')
                uniq = input()
                while uniq not in {'1', '2'}:
                    print('Введи 1 или 2')
                    uniq = input()

        with open('settings_' + name + name_id + '.json', 'w', encoding="utf-8") as settings:
            settings.write(f'{answer_numbers}{show_setting}{change_mod}{name}\n{save_mistakes}\n{uniq}')
        with open('settings.json', 'w', encoding="utf-8") as all_settings:
            settings_json = {
                'change_mod': change_mod ,
                'name': name,
                'name_id': name_id}
            json.dump(settings_json, all_settings, ensure_ascii=False)

    if mode == '3':
        fix_mistakes()

    elif mode == '0':
        print('До скорых встреч!')
        if isfile('mistakes_' + name + name_id + '.txt'):
            new_file_name = remove_same_lines(('mistakes_' + name + name_id + '.txt'))
            remove(('mistakes_' + name + name_id + '.txt'))
            rename(new_file_name, ('mistakes_' + name + name_id + '.txt'))
        break
    else:
        pass
# TODO: