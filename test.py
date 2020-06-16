from time import sleep
from timeit import default_timer
from threading import Thread


def hello(name, surname):
    sleep(3)
    print('Привет ', name, surname)


for i in range(3):
    t = Thread(target=hello, args=['Слава', 'Сальников'], name=f'potok{i+1}')
    t.start()

t.join()
print(default_timer())
