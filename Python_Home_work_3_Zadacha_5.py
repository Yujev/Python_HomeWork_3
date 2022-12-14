# Задача_5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число: '))


def fibonacci(k):
    nums = []
    a, b = 1, 1
    for i in range(k):
        nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(-1, k):
        nums.insert(0, a)
        a, b = b, a - b
    return nums


nums = fibonacci(k)

print("Твой результат:")
print(fibonacci(k))

