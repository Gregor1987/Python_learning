# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Var_1
some_list = [int(input(f'Введите число {i + 1}: ')) for i in range(int(input(f'введите количество элементов: ')))]
print(some_list)
summ = 0
for i in range(len(some_list)):
    if i % 2 != 0:
        summ += some_list[i]
print(f'сумма эелементов на нечетных позициях: {summ}')

# Var_2
some_list = [int(input(f'Введите число {i + 1}: ')) for i in range(int(input(f'введите количество элементов: ')))]
print(some_list)
summ = 0
for i in range(1, len(some_list), 2):
    summ += some_list[i]
print(f'сумма эелементов на нечетных позициях: {summ}')

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

some_list = [int(input(f'Введите число {i + 1}: ')) for i in range(int(input(f'введите количество элементов: ')))]
print(some_list)
result_list = []
for i in range((len(some_list) + 1) // 2):
    result_list.append(some_list[i] * some_list[len(some_list) - i - 1])
print(result_list)

# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

some_list = [float(input(f'Введите число {i + 1}: ')) for i in range(int(input(f'введите количество элементов: ')))]
decimals_list = []
for i in range(len(some_list)):
    if some_list[i] % 1 != 0:
        decimals_list.append(some_list[i] % 1)
max_el = decimals_list[0]
min_el = decimals_list[0]
for i in range(1, len(decimals_list)):
    if decimals_list[i] > max_el:
        max_el = decimals_list[i]
    elif decimals_list[i] < min_el:
        min_el = decimals_list[i]
print(round(max_el - min_el, 2))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное

# Var_1
num = int(input('введите число: '))
print(f'число {num} в двоичной системе: {num:b}')

# Var_2
num = int(input('введите число: '))
print(f'число {num} в двоичной системе: ', end='')
binary_number = []
while num != 0:
    binary_number.insert(0, str(num % 2))
    num //= 2
for i in range(len(binary_number)):
    print(binary_number[i], end='')

# Var_3
num = int(input('введите число: '))
print(f'число {num} в двоичной системе: ', end='')
binary_number = ''
while num != 0:
    binary_number = ''.join((str(num % 2), binary_number))
    num //= 2
print(binary_number)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input('введите число: '))
fibonacci = [0, 1]
for i in range(2, k + 1):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
negafibonacci = [0, 1]
for i in range(2, k + 1):
    negafibonacci.append(negafibonacci[i - 2] - negafibonacci[i - 1])
total_fibonacci = [0]
for i in range(1, len(negafibonacci)):
    total_fibonacci.insert(0, negafibonacci[i])
    total_fibonacci.append(fibonacci[i])
print(f'Список чисел Фибоначчи для k = {k}:\n{total_fibonacci}')