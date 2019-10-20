from random import randint, choice
from timeit import default_timer

#Выводит затраченное время
def minutes(time):
    if time>60:
        minutes = time//60 #Целое число минут, без остатка
        
        #Склонение минут
        if minutes == 1:
            minutesText = ( str(minutes) + ' минуту')
        elif 1<minutes<5:
            minutesText = ( str(minutes) + ' минуты')
        elif 4<minutes<21:
            minutesText = (str(minutes) + ' минут')
            
        seconds = time-minutes*60 #Остаток секунд
        text = ('Ты справился за ' + minutesText + ' и ' + str(seconds))
    else:
        seconds = time
        text = ('Ты справился за ' + str(seconds))

    timeStr = str(time)
    timeCut = timeStr[-1]  #Последняя цифра в числе секунд
    timeCut = int(timeCut)

    # Склонение секунд
    if timeCut == 1:
        print(text + ' секунду')
    elif 1<timeCut<5:
        if 9<time<15:
            print(text + ' секунд')
        else:
            print(text + ' секунды')
    elif timeCut>4 or timeCut == 0:
        print(text + ' секунд')



print('Привет! Меня зовут Роджер. А тебя?')
name = input()
name = name.title()
print('Приятно познакомиться, ' + name)
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

        #Выводит статистику
        minutes(answers_time)
        print('Правильных ответов:' + str(rights))
        print('Неправильных ответов:' + str(fails))
        
        
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