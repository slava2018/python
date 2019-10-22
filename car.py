print('введите комманду')

engine_status = 0 # Выключен

command=input()
if command not in {'on','off','exit','help','status'}:
    print('Вы ввели неверную комманду, чтобы увидеть список всех комманд, введите "help" ')
else:
    if command == 'on':
        if engine_status == 1:
            print('')
        else:
            print('')
            engine_status = 1

    if command == 'off':
        if engine_status == 0:
            print('')
        else:
            print('')
            engine_status = 0
    if command == 'exit':
        print('')
    if command == 'help':
        print('')
    if command == 'status':
        print('')