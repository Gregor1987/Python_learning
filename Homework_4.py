# Вычислить число c заданной точностью d

# Var_1
num = float(input('введите число: '))
d = input('введите точность: ')
print(round(num, len(d) - 2))

# Var_2
num = float(input('введите число: '))
d = input('введите точность: ')
print(f'%.{len(d.split(".")[1])}f'%num)

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

num = int(input('введите число: '))
some_list = []
for i in range(2, num + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        if num % i == 0:
            some_list.append(i)
print(some_list)

# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности

# Var_1

num_list = sorted(map(int, input('введите последовательность чисел через пробел:\n').split()))
unique_num_list = [num_list[0]]
for i in range(1, len(num_list)):
    if num_list[i] != num_list[i - 1]:
        unique_num_list.append(num_list[i])
print(unique_num_list)

# Var_2

print(set(map(int, input('введите последовательность чисел через пробел:\n').split())))

# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random
def super_symbol(n): # преобразует число в надстрочный символ для записи в файл
    n = str(n)
    result = ''
    for i in range(len(n)):
        if int(str(n)[i]) == 1:
            result += str(chr(0x00b9))
        elif 1 < int(str(n)[i]) <= 3:
            result += str(chr(0x00b0 + int(str(n)[i])))
        else:
            result += str(chr(0x2070 + int(str(n)[i])))
    return result
k = int(input('введите число: '))
polynomial = random.randint(0, 100)
free_coef_check = bool
if polynomial == 0:
    free_coef_check = False
coef = random.randint(0, 100)
if coef != 0:
    polynomial = f'{coef}x' + ' + ' + str(polynomial)
elif coef == 1:
    polynomial = f'x' + ' + ' + str(polynomial)
for i in range(2, k + 1):
    coef = random.randint(0, 100)
    if coef != 0:
        polynomial = f'{coef}x{super_symbol(i)}' + ' + ' + str(polynomial)
    elif coef == 1:
        polynomial = f'x{super_symbol(i)}' + ' + ' + str(polynomial)
if not free_coef_check:
    polynomial = polynomial[:-3]
with open('polynomial.txt', 'w+', encoding='utf8') as file:
    file.write(polynomial + ' = 0')
