#! /usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import default_timer


# функция-декоратор для получения времени выполнения функции
def show_time(func):
    # функция-обёртка
    def wrapper(*args, **kwargs):

        start = default_timer()
        result = func(*args, **kwargs)  # вызов функции
        stop = default_timer()

        spent_time = f'{round(stop-start, 8)} seconds'
        print(spent_time)
        # вернём  результат выполнения функции
        return result

    return wrapper


# функция создания списка чётных чисел через цикл for
@show_time  # синтаксический сахар для вызова декоратора
def even_numbers1(n):
    numbers = []
    for i in range(2, n+2, 2):
        numbers.append(i)
    return numbers


# функция создания списка чётных чисел через генератор списка
# @show_time
def even_numbers2(n):
    numbers = [i for i in range(2, n+2, 2)]
    return numbers


# вызов функции с использованием декоратора c синтаксическим сахаром @show_time
even_numbers1(10000000)

# прямое использование декоратора без синтаксического сахара @show_time
received_func = show_time(even_numbers2)
a = received_func(10000000)
