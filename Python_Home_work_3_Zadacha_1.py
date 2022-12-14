# Задача_1.# Последний элемент
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint

n = 5       # Размер списка
master = 1    # Первый элемент
second = 5    # Последний элемент


def list(n, master, second):
    return [randint(master, second) for i in range(n)]  # Получаю список из случайных элементов


def sum_odd(my_list):  # Получаю сумму элементов на нечетных индексах
    return sum(my_list[1::2])


my_list = list(n, master, second)

print(f'Твой список случайных чисел: \n{my_list}')
print('Сумма элементов на нечетных индексах: ')
print(sum_odd(my_list))
