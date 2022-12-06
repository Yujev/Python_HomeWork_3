# Задача_2
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

from random import randint

n = 5       # Размер списка
master = 1  # Первый элемент
second = 5 # Последний элемент


def new_list(n, master, second):
    return [randint(master, second) for i in range(n)]  # Получаю список из случайных элементов


my_list = new_list(n, master, second)
print(f'Твой список случайных чисел: \n{my_list}')


def list2(k):   # Считаю произведение пар элементов
    res = []
    while len(k) > 1:
        res.append(k[0] * k[-1])
        del k[0]
        del k[-1]
    if len(k) == 1: res.append(k[0] ** 2)   # Возвожу серединный элемент в степень
    return res

print('Произведение пар чисел списка: ')
print(list2(my_list))

