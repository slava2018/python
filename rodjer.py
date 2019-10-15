from random import randint, choice
from timeit import default_timer

def minutes(time):
    if time>60:
        minutes = time//60 #Целое число минут, без остатка
        seconds = time-minutes*60 #Остаток секунд
        text = ('Ты справился за ' + str(minutes) + 'минут и ' + str(seconds))
    else:
        seconds = time
        text = ('Ты справился за ' + str(seconds))

    times = str(time)
    timek = times[-1] #Последняя цифра в числе секунд
    timek = int(timek)

    if timek == 1:
        print(text + ' секунду')
    elif 1<timek<5:
        if 9<time<15:
            print(text + ' секунд')
        else:
            print(text + ' секунды')
    elif timek>4 or timek == 0:
        print(text + ' секунд')



print('Привет! Меня зовут Роджер. А тебя?')
name = input()
name = name.title()
print('Приятно познакомиться,' + name)
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

        while not examples_quantity.isdigit():
            print(name + ',сколько примеров ты готов решить?')
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


        for example in range(int(examples_quantity)):
            print('Пример ' + str(example+1) + ':')

            maximum_answer = int(maximum_answer)

            number1 = randint(1,maximum_answer)
            number2 = randint(1,maximum_answer)
            sign = choice('+-')

            if number2 > number1:
                sign = '+'

            while number2 + number1 > maximum_answer:
                number1 = randint(1, maximum_answer)
                number2 = randint(1, maximum_answer)

            answer = ''  # Ответ

            while not answer.isdigit():
                print('Сколько будет ' + str(number1) + sign + str(number2) + '?')
                start = default_timer() # начало отсчета
                answer = input()
                stop = default_timer()  # конец отсчёта

                if not answer.isdigit():
                    print('Ты ошибся, введи цифру')

                answers_time += round(stop - start)

            answer = int(answer)

            if sign == '+':
                right_answer = number1 + number2


            if sign == '-':
                right_answer = number1 - number2



            fails = 0
            rights = 0

            if answer == right_answer:
                rights += 1
                print('Правильно.')
            else:
                fails += 1
                print('Неправильно. Правильный ответ:'+ str(right_answer))

        minutes(answers_time)
        print('Правильных ответов:' + str(rights))
        print('Неправильных ответов:' + str(fails))
        print('Хочешь сыграть еще?')
        repeat = input()
        while repeat not in {'да', 'нет'}:
            print('''Ты ошибся, должно быть 'да' или 'нет'.
            Введи заново.''')
            repeat = input()
            repeat = repeat.lower()
        if repeat == 'нет':
            print('Хорошо,' + name + '. Ты сегодня неплохо поработал!')
            print('Пока')

    else:
        print('''Передумал? Хорошо, как-нибудь в другой раз...
Пока!''')
        repeat = 'нет'