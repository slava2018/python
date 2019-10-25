print('Введите комманду')

engine_status = 0 # Выключен
start = 1

while start == 1:
    command=input()
    if command not in {'on','off','exit','help','status'}:
        print('Вы ввели неверную комманду, чтобы увидеть список всех комманд, введите "help" ')
    else:
        if command == 'on':
            if engine_status == 1:
                print('Двигатель уже работает.')
            else:
                print('Двигатель заведен.')
                engine_status = 1

        if command == 'off':
            if engine_status == 0:
                print('Двигатель уже заглушен.')
            else:
                print('Двигатель заглушен.')
                engine_status = 0

        if command == 'exit':
            if engine_status == 1:
                print('Выходить из едущей машины не рекоммендуется.')
            else:
                print('Вы вышли из машины.')
                start = 0

        if command == 'help':
            print('''off - Заглушить двигатель.
on - Завести двигатель.
exit - Выйти из машины.
help - Вывести список всех комманд.
status - Показать статус двигателя.
''')

        if command == 'status':
            if engine_status == 1:
                print('Двигатель работает.')
            else:
                print('Двигатель заглушен.')