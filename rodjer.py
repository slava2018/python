from random import randint, choice
from timeit import default_timer
from os.path import isfile
from os import rename, remove
from lib import time_endings, seconds_convert

def answer_generation(number1, number2, sign):

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

    example_line =  [number1, sign, number2]
    return example_line

def create_mistakes_file(name, mistake):
    file_name = ('mistakes_' + name + '2.txt')
    if isfile(file_name):
        with open(file_name, 'a') as new_mistakes:
            new_mistakes.write(mistake)
    else:
        with open(file_name, 'w') as new_mistakes:
            new_mistakes.write(mistake)

def choise_2(answer):
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


print('Привет! Меня зовут Роджер. А тебя?')
name = input()
name = name.title()
print('Приятно познакомиться, ' + name)
if isfile('mistakes_' + name + '.txt'):

    print('Хочешь поработать над ошибками?')
    mistakes_ready = input()
    choise_2(mistakes_ready)

    if mistakes_ready == 'да':
        answer = 1
        with open(('mistakes_' + name + '.txt'), 'r') as mistakes_file:
            print('Хорошо, начнем.')

            m_example = mistakes_file.readline()
            while m_example != '':
                while answer != 'стоп':
                    print(m_example)
                    answer = input()
                    number1,number2,sign = m_example.split()
                    right_answer = answer_generation(number1, number2, sign)

                    if answer != 'стоп':
                        if int(answer) == int(right_answer) :
                            print('Правильно! Следующий пример:')
                        else:
                            print('Ты ошибся.')
                            # Создает или открывает новый файл с ошибками
                            create_mistakes_file(name, m_example)
                        print('Если устал, напиши "стоп".')
                m_example = ''
                print('Устал? Хорошо, ты можешь продолжить исправлять свои ошибки позже.')
                # Дописывает строчки из прошлого файла в новый
                while mistakes_file.readline() != '':
                    create_mistakes_file(name, m_example)

        # Переименовывает новый файл и удаляет старый
        remove('mistakes_' + name + '.txt')
        rename(('mistakes_' + name + '2.txt'),('mistakes_' + name + '.txt'))

print('''Давай проверим твои знания в математике.
Ты готов?('да' или 'нет')''')
ready = input()

repeat = 'да'
while repeat == 'да':
    choise_2
    if ready == 'да':
        examples_quantity = '' #Количество примеров
        maximum_answer = '' #Максимальное число
        answers_time = 0  # Время ответов

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

        # Генерирует и выводит пример

        for example_kol in range(int(examples_quantity)):
            print('Пример ' + str(example_kol + 1) + ':')
            example_line = example_generation(maximum_answer)
            number1, number2, sign = example_line.split()
            right_answer = answer_generation(number1, number2, sign)

            example = (str(number1) + str(sign) + str(number2))
            print('Сколько будет' + example + '?')

            start = default_timer()  # начало отсчета
            answer = input()
            stop = default_timer()  # конец отсчёта
            answers_time += round(stop - start)  # Время ответа

            # Продолжается пока пользователь не введет положительное число
            choise_digit(answer)
            answer = int(answer)
            #Считает количество правильных и неправильных ответов
            if answer == right_answer:
                rights += 1
                print('Правильно.')
            else:
                fails += 1
                print('Неправильно.')

                #Создание файла с ошибками

                with open(('mistakes_' + name + '.txt'), 'a') as mistakes:
                    mistakes.write(f'{example}\n')


        print('Правильных ответов:' + str(rights))
        print('Ошибок:' + str(fails))
        print('Ты справился за' + seconds_convert(answers_time))
        
        
        print('Хочешь сыграть еще?')
        repeat = input()
        choise_2
            
        #Завершает работу
        if repeat == 'нет':
            print('Хорошо, ' + name + '. Ты сегодня неплохо поработал!')
            print('Пока')
            
    # Завершает работу
    else:
        print('''Передумал? Хорошо, как-нибудь в другой раз...
Пока!''')
        repeat = 'нет'