from random import randint, choice
from timeit import default_timer
from os.path import isfile
from os import rename, remove
from slava_lib import time_endings, seconds_convert

print('Привет! Меня зовут Роджер. А тебя?')
name = input()
name = name.title()
print('Приятно познакомиться, ' + name)

if isfile('mistakes_' + name + '.txt'):

    print('Хочешь поработать над ошибками?')
    mistakes_ready = input()
    while mistakes_ready not in {'да', 'нет'}:
        print('''Ты ошибся, должно быть 'да' или 'нет'.
    Введи заново.''')
        mistakes_ready = input()

    if mistakes_ready == 'да':
        answer = 1
        with open(('mistakes_' + name + '.txt'), 'r') as mistakes_file:

            print('Хорошо, начнем.')

            m_example = mistakes_file.readline()
            while m_example != '':
                while answer != 'стоп':
                    print(m_example)
                    answer = input()
                    m_right_answer = mistakes_file.readline()
                    if answer != 'стоп':
                        if int(answer) == int(m_right_answer):
                            print('Правильно! Следующий пример:')
                        else:
                            print('Ты ошибся.')
                            # Создает новый файл с ошибками
                            new_mistakes = open(('mistakes_' + name + '2.txt'),'w')
                            new_mistakes.write(m_example)
                            new_mistakes.write(m_right_answer)
                            new_mistakes.close()
                        m_example = mistakes_file.readline()
                        print('Если устал, напиши "стоп".')
                if answer == 'стоп':
                    m_example = ''
                    print('Устал? Хорошо, ты можешь продолжить исправлять свои ошибки позже.')
                    # Дописывает строчки из прошлого файла в новый
                    new_mistakes = open(('mistakes_' + name + '2.txt'), 'w')
                    new_mistakes.write(m_example)
                    new_mistakes.write(m_right_answer)
                    new_mistakes.close()
                    while mistakes_file.readline() != '':
                        new_mistakes = open(('mistakes_' + name + '2.txt'), 'a')
                        new_mistakes.write(mistakes_file.readline())
                        new_mistakes.close()


        # Переименовывает новый файл и удаляет старый
        remove('mistakes_' + name + '.txt')
        rename(('mistakes_' + name + '2.txt'),('mistakes_' + name + '.txt'))

print('''Давай проверим твои знания в математике.
Ты готов?('да' или 'нет')''')
ready = input()

repeat = 'да'
while repeat == 'да':

    while ready not in {'да', 'нет'}:
        print('''Ты ошибся, должно быть 'да' или 'нет'.
Введи заново.''')
        ready = input()

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
                    while not examples_quantity.isdigit():
                        print('Ты ошибся, введи цифру')
                        examples_quantity = input()
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
                    while not maximum_answer.isdigit():
                        print('Ты ошибся, введи цифру')
                        maximum_answer = input()
            else:
                print('Ты ошибся, введи цифру')

        print('Хорошо, тогда начинаем...')

        fails = 0
        rights = 0

        # Генерирует и выводит пример
        for example in range(int(examples_quantity)):
            print('Пример ' + str(example+1) + ':')

            maximum_answer = int(maximum_answer) #Максимально возможное число

            #Первая версия примера
            number1 = randint(1,maximum_answer)
            number2 = randint(1,maximum_answer)
            sign = choice('+-')

            # Проверка соответствия правилам
            while number2 + number1 > maximum_answer:
                number1 = randint(1, maximum_answer)
                number2 = randint(1, maximum_answer)

            if number2 > number1:
                sign = '+'

            answer = ''  # Ответ

            # Продолжается пока пользователь не введет положительное число
            while not answer.isdigit():
                print('Сколько будет ' + str(number1) + sign + str(number2) + '?')
                start = default_timer() # начало отсчета
                answer = input()
                stop = default_timer()  # конец отсчёта
                if not answer.isdigit():
                    print('Ты ошибся, введи цифру')
                answers_time += round(stop - start) #Время ответа

            answer = int(answer)

            #Генерирует правильный ответ
            if sign == '+':
                right_answer = number1 + number2
            if sign == '-':
                right_answer = number1 - number2

            #Считает количество правильных и неправильных ответов
            if answer == right_answer:
                rights += 1
                print('Правильно.')
            else:
                fails += 1
                print('Неправильно. Правильный ответ: '+ str(right_answer))

                #Создание файла с ошибками

                with open(('mistakes_' + name + '.txt'), 'a') as mistakes:
                    mistakes.write(f'{number1} {sign} {number2}\n')


        print('Правильных ответов:' + str(rights))
        print('Ошибок:' + str(fails))
        print(seconds_convert(answers_time))
        
        
        print('Хочешь сыграть еще?')
        repeat = input()
        
        #Проверяет соответствие правилу
        while repeat not in {'да', 'нет'}:
            print('''Ты ошибся, должно быть 'да' или 'нет'.
            Введи заново.''')
            repeat = input()
            repeat = repeat.lower()
            
        #Завершает работу
        if repeat == 'нет':
            print('Хорошо, ' + name + '. Ты сегодня неплохо поработал!')
            print('Пока')
            
    # Завершает работу
    else:
        print('''Передумал? Хорошо, как-нибудь в другой раз...
Пока!''')
        repeat = 'нет'