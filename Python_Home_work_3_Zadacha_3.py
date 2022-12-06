# Задача_3.
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

n = 5       # Размер списка
master = 1  # Первый элемент
second = 5  # Последний элемент


def get_list(n, master, second):  # Получаю список из случайных элементов
    return [round(uniform(master, second), 3) for i in range(n)]  # Возвращаю список со случайными вещественными числами. После "." три знака округления


def find_diff(my_numbers):  # Ищу разницу между максимальным и минимальным значением дробной части
    numbers = [round(x - int(x), 2) for x in (my_numbers)]
    return max(numbers) - min(numbers)


my_list = get_list(n, master, second)

print(f'Твой список случайных чисел: \n{my_list}')
print('Твой результат: ')
print(find_diff(my_list))
