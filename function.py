def check_input(user_input, odz, warnings):
    last_odz = odz[-1]
    while user_input not in odz:
        if warnings:
            print(f'Должно быть {odz} или {last_odz}')
        else:
            print('некорректный ввод')
        user_input = input('Введи другое значение:')
    return user_input
