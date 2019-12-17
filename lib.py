# функция временных окончаний
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
        
        
# функция перевода секунд
def seconds_convert(time_in_seconds):
    
    if time_in_seconds < 60:
        spent_time = f' за {time_in_seconds} секунд{time_endings(time_in_seconds)}'
    else:
        minutes = time_in_seconds // 60  # Целое число минут, без остатка
        seconds = time_in_seconds - minutes * 60  # Остаток секунд
        if time_in_seconds-minutes*60==0:
            spent_time = f' за {minutes} минут{time_endings(minutes)}'
        else:
            spent_time = f' за {minutes} минут{time_endings(minutes)} и {seconds} секунд{time_endings(time_in_seconds)}'

    return spent_time

#Удаление дупликатов в файле
def duplicats(file_name):

    all_lines = []

    with open(file_name, 'r') as old_file:
        line = old_file.readline()
        while line:
            all_lines.append(line)
            line = old_file.readline()

    all_lines = set(all_lines)
    new_file_name = ('2'+file_name)
    with open(new_file_name, 'w') as new_file:
        for line in all_lines:
            new_file.write(line)
    return new_file_name
