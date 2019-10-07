from random import randint, choice
from timeit import default_timer


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

        while examples_quantity.isdigit() != True:
            print(name + ',сколько примеров ты готов решить?')
            examples_quantity = input()
            if examples_quantity.isdigit() != True:
                print('Ты ошибся, введи цифру')

        while maximum_answer.isdigit() != True:
            print('До скольки будем считать? Например до 100.')
            maximum_answer = input()
            if maximum_answer.isdigit() != True:
                print('Ты ошибся, введи цифру')

        print('Хорошо, тогда начинаем...')


        for example in range(int(examples_quantity)):
            print('Пример ' + str(example+1) + ':')

            maximum_answer = int(maximum_answer)

            number1 = randint(1,maximum_answer)
            number2 = randint(1,maximum_answer)
            sign = choice('+-')

            answer = ''  # Ответ
            answers_time = 0 # Время ответов
            while answer.isdigit() != True:
                print('Сколько будет ' + str(number1) + sign + str(number2) + '?')
                start = default_timer() # начало отсчета
                answer = input()
                if answer.isdigit() != True:
                    print('Ты ошибся, введи цифру')
                else:
                    stop = default_timer()  # конец отсчёта
                    answers_time += round(stop - start)

            answer = int(answer)

            if sign == '+':
                right_answer = number1 + number2
            if sign == '-':
                right_answer = number1 - number2

            fails = 0
            rights = 0

            if answer == right_answer:
                rights += rights + 1
                print('Правильно.')
            else:
                fails += fails +1
                print('Ты ошибся, попробуй еще.')
                print('Сколько будет ' + str(number1) + sign + str(number2) + '?')
                start = default_timer()
                answer = input()
                stop = default_timer()
                answer = int(answer)
                answers_time += round(stop - start)
                if answer != right_answer:
                    print('Неправильно. Правильный ответ:'+ str(right_answer))
        print('Затраченное время:' + str(answers_time) + 'секунд')
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