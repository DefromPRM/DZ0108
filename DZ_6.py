from random import randint

# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1 = int(input("Введите первый элемент прогрессии: "))
# n = int(input("Введите количество элементов прогрессии: "))
# d = int(input("Введите разность элементов прогрессии: "))


# def aprogress(result):
#     result = []
#     for i in range(n):
#         an = a1 + i * d
#         result.append(an)
#     return result


# print(*aprogress(n), sep="\n")


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного
# максимума)

# sp = [randint(-10, 100) for i in range(10)]
# print(sp)


# def defining_indexes(result):
#     result = []
#     min_value = int(input("Введите минимальное значение элемента: "))
#     max_value = int(input("Введите максимальное значение элемента: "))
#     for i in range(len(sp)):
#         if min_value <= sp[i] <= max_value:
#             result.append(i)
#     return result


# print(defining_indexes(sp))
