from datetime import datetime
from pprint import pprint


# Функция декоратор
def show_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        stop = datetime.now()
        spent_time = stop - start
        print(spent_time)
        return result
    return wrapper


@show_time
def numbers1(n):
    lst = []
    for i in range(n):
        if i % 2 == 0:
            lst.append(i)
    return lst


@show_time
def numbers2(n):
    lst = [i for i in range(n) if i % 2 == 0]
    return lst


# n = show_time(numbers1)
# a = n(100000)
#print(a)

numbers2(10**5)
