from random import randint, choice

print('Привет! Меня зовут Роджер. А тебя?')
name = input()
name = name.title()
print('Приятно познакомиться,' + name)
print('''Давай проверим твои знания в математике.
Ты готов?('да' или 'нет')''')
ready = input()

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

    fails = 0
    rights = 0

    for example in range(int(examples_quantity)):
        print('Пример ' + str(example+1) + ':')

        maximum_answer = int(maximum_answer)

        number1 = randint(1,maximum_answer)
        number2 = randint(1,maximum_answer)
        sign = choice('+-')

        print('Сколько будет ' + str(number1) + sign + str(number2) + '?')
        answer = input()

        if sign == '+':
            right_answer = number1 + number2
        if sign == '-':
            right_answer = number1 - number2

        if answer == right_answer:
            rights += 1
        else:
            fails += 1




else:
    print('''Передумал? Хорошо, как-нибудь в другой раз...
    Пока!''')