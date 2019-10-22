from random import randint, choice
from timeit import default_timer

#Выводит затраченное время
def time_endings(v):

    v_str = str(v)
    v_last = int(v_str[-1])

    if 9<v<20:
        return ''
    else:
        if v_last == 1:
            return 'у'
        if 1<v_last<5:
            return 'ы'
        else:
            return ''

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
        if answers_time < 60:
            print('Ты справился за ' + str(answers_time) + ' секунд' + time_endings(answers_time))
        else:
            minutes = answers_time // 60  # Целое число минут, без остатка
            seconds = answers_time - minutes * 60  # Остаток секунд
            if answers_time-minutes*60==0:
                print('Ты справился за ' + str(minutes) + ' минут' + time_endings(minutes))
            else:
                print('Ты справился за ' + str(minutes) + ' минут' + time_endings(minutes) + ' и ' + str(seconds) + ' секунд' +
                      time_endings(seconds))
        print('Правильных ответов:' + str(rights))
        print('Ошибок:' + str(fails))
        
        
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