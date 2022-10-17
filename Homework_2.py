# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = int(input('введите число: ').replace('.', ''))
sum_of_numbers = 0
while num != 0:
    sum_of_numbers = sum_of_numbers + num % 10
    num = num // 10
print(sum_of_numbers)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

num = int(input('введите число: '))
list_factorial = []
for i in range(1, num + 1):
    result = 1
    for n in range(1, i + 1):
        result = result * n
    list_factorial.append(result)
print(list_factorial)

# Задайте список из n чисел последовательности (1 + 1 / n)^n и выведите на экран их сумму.

n = int(input('введите число: '))
sum = 0
for i in range (1, n + 1):
    num = (1 + 1 / i) ** i
    sum += num
print(f'{n}: {round(sum, 2)} ')

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
n = int(input('введите число: '))
some_list = list(range(-n, n + 1))
for i in range(1, len(some_list) - 1):
    temp_index = random.randint(1, len(some_list) - 2)
    temp = some_list[temp_index]
    some_list[temp_index] = some_list[i]
    some_list[i] = temp
print(some_list)
list_multiply_index = []
with open('file.txt', 'w+') as f:
    for _ in range(random.randint(1, n - 1)):
        f.write(f'{random.randint(0, n - 1)}\n')
    f.seek(0)
    for line in f:
        list_multiply_index.append(line)
result = 1
for i in range(len(list_multiply_index)):
    result *= some_list[int(list_multiply_index[i])]
print(result)

# Реализуйте алгоритм перемешивания списка.

import random
n = int(input('введите количество элементов: '))
some_list = list(range(n))
print(some_list)
for i in range(n):
    temp_index = random.randint(0, n - 1)
    temp = some_list[temp_index]
    some_list[temp_index] = some_list[i]
    some_list[i] = temp
print(some_list)

# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

list_1 = [1, 2, 3, 2, 0]
list_2 = [5, 1, 2, 7, 3, 2]
list_3 = []
for i in range(len(list_1)):
    for j in range(len(list_2)):
        if list_1[i] == list_2[j]:
            list_3.append(list_1[i])
            break
print(list_3)