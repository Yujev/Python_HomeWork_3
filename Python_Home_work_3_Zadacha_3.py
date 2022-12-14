# Задача_3.
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from random import uniform, randint

n = 5  # Размер списка
master = 1  # Первый элемент
second = 5  # Последний элемент


def get_list(n, master, second):
    a = []
    i = 0
    for (i) in range(n):
        if randint(0, 1):
            a.append(randint(master, second))
        else:
            a.append(uniform(master, second))
        i += 1
    return a


def find_diff(my_numbers):
    numbers = [round(x - int(x), 2) for x in (my_numbers)]
    return max(numbers) - min(numbers)


my_list = get_list(n, master, second)

print(f'Твой список случайных чисел: \n{my_list}')
print('Твой результат: ')
print(find_diff(my_list))
