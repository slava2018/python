# Игра "Угадай число"
import random
print('Привет! Как тебя зовут?')
name = input()

def guessNumber():
    print('Что ж, ' + name + ', я загадываю число от 1 до 20.')

    number = random.randint(1, 20)

    counter = 0
    for counter in range(6):
        if counter == 0:
            print('Попробуй угадать:')
        else:
            print('Попробуй угадать снова:')

        guess_number = int(input()) #Загаданное число

        if guess_number > number:
            print('Твое число слишком большое.')
        if guess_number < number:
            print('Твое число слишком маленькое.')
        if guess_number == number:
            break

    if guess_number == number:
        counter = str(counter+1)
        print('Отлично, ' + name + '! Ты справился за ' + counter + ' попытки!')

    if guess_number != number:
        number = str(number)
        print('Увы, ты не угадал, я загадал число ' + number)


play_again = 'да'
while play_again == 'да':
    guessNumber()
    print('Хочешь сыграть еще раз? (\'да\',\'нет\')')
    play_again = input()