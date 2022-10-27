# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

initial_text = list(input().split())
result_text = ''
for i in initial_text:
    if 'абв' not in i:
        result_text += i + ' '
print(result_text)

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

import random


def win_condition(candies):
    win = False
    if candies <= 0:
        win = True
        print(f'No candies left\n'
              f'Player {i % 2 + 1} wins')
    return win


def player_turn(message):
    turn = int(input(message))
    while not (28 >= turn >= 1):
        turn = player_turn('incorrect number of candies, please try again: ')
    return turn


candies = 2021
dice = random.randint(1, 2)
if dice == 1:
    print(f'Player {dice} goes first')
    for i in range(2022):
        print(f'Player {i % 2 + 1} turn')
        candies -= player_turn('please take from 1 to 28 candies: ')
        if win_condition(candies):
            break
        else:
            print(f'{candies} left')
else:
    print(f'Player {dice} goes first')
    for i in range(1, 2023):
        print(f'Player {i % 2 + 1} turn')
        candies -= player_turn('please take from 1 to 28 candies: ')
        if win_condition(candies):
            break
        else:
            print(f'{candies} left')

# a) Добавьте игру против бота

import random


def win_condition(candies):
    win = False
    if candies <= 0:
        win = True
        print(f'No candies left\n'
              f'Player {i % 2 + 1} wins')
    return win


def player_turn(message):
    if not (i % 2):
        turn = int(input(message))
        while not (28 >= turn >= 1):
            turn = player_turn('incorrect number of candies, please try again: ')
    elif candies <= 28:
        turn = candies
    else:
        turn = random.randint(1, 28)
        print(f'Bot takes {turn} candies')
    return turn


candies = 2021
dice = random.randint(1, 2)
if dice == 1:
    print('Player goes first')
    for i in range(2022):
        candies -= player_turn('please take from 1 to 28 candies: ')
        if win_condition(candies):
            break
        else:
            print(f'{candies} left')
else:
    print('Bot goes first')
    for i in range(1, 2023):
        candies -= player_turn('please take from 1 to 28 candies: ')
        if win_condition(candies):
            break
        else:
            print(f'{candies} left')

# b) Подумайте как наделить бота ""интеллектом""

import random


def win_condition(candies):
    win = False
    if candies <= 0:
        win = True
        print(f'{candies} candies left')
        if i % 2 == 0:
            print(f'Player wins')
        else:
            print(f'Bot wins')
    return win


def player_turn(message):
    if i % 2 == 0:
        turn = int(input(message))
        while not (28 >= turn >= 1):
            turn = player_turn('incorrect number of candies, please try again: ')
    elif candies <= 28:
        turn = candies
        print(f'Bot takes {turn} candies')
    else:
        turn = candies - 29 * ((140 - i) // 2)
        if turn == 0:
            turn = random.randint(1, 28)
        print(f'Bot takes {turn} candies')
    return turn


candies = 2021
dice = random.randint(1, 2)
if dice == 1:
    print('Player goes first')
    for i in range(140):
        candies -= player_turn('please take from 1 to 28 candies: ')
        if win_condition(candies):
            break
        else:
            print(f'{candies} left')
else:
    print('Bot goes first')
    for i in range(1, 141):
        candies -= player_turn('please take from 1 to 28 candies: ')
        if win_condition(candies):
            break
        else:
            print(f'{candies} left')


# Создайте программу для игры в ""Крестики-нолики"".

# Var_1 Player vs Player

def print_field(field_el):
    print(f'{field_el[0]} {field_el[1]} {field_el[2]}\n'
          f'{field_el[3]} {field_el[4]} {field_el[5]}\n'
          f'{field_el[6]} {field_el[7]} {field_el[8]}')


def win_condition(n, x):
    win = False
    if ((n[0] == x and n[1] == x and n[2] == x) or
            (n[3] == x and n[4] == x and n[5] == x) or
            (n[6] == x and n[7] == x and n[8] == x) or
            (n[0] == x and n[4] == x and n[8] == x) or
            (n[6] == x and n[4] == x and n[2] == x) or
            (n[0] == x and n[3] == x and n[6] == x) or
            (n[1] == x and n[4] == x and n[7] == x) or
            (n[2] == x and n[5] == x and n[8] == x)):
        win = True
        print_field(field)
        print(f'Player {i % 2 + 1} wins!')
        return win


def player_turn(message):
    turn = list(map(int, input(message).split()))
    if i % 2 == 0:
        x = ' X '
    else:
        x = ' 0 '
    while len(turn) != 2 or not (3 >= turn[0] >= 1) or not (3 >= turn[1] >= 1):
        turn = list(map(int, input('not acceptable move, please try again: ').split()))
    if turn[0] == 1:
        if field[turn[1] - 1] != ' - ':
            player_turn('such turn has already been made, please try again: ')
        else:
            field[turn[1] - 1] = x
    elif turn[0] == 2:
        if field[turn[1] + 2] != ' - ':
            player_turn('such turn has already been made, please try again: ')
        else:
            field[turn[1] + 2] = x
    else:
        if field[turn[1] + 5] != ' - ':
            player_turn('such turn has already been made, please try again: ')
        else:
            field[turn[1] + 5] = x
    return x


field = [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
print_field(field)
for i in range(9):
    if win_condition(field, player_turn('please input string and column numbers divided by space: ')):
        break
    else:
        print_field(field)
    if i == 8:
        print('Draw')

# Var_2 Player vs Bot

import random


def print_field(field_el):
    print(f'{field_el[0]} {field_el[1]} {field_el[2]}\n'
          f'{field_el[3]} {field_el[4]} {field_el[5]}\n'
          f'{field_el[6]} {field_el[7]} {field_el[8]}')


def win_condition(n, x):
    win = False
    if ((n[0] == x and n[1] == x and n[2] == x) or
            (n[3] == x and n[4] == x and n[5] == x) or
            (n[6] == x and n[7] == x and n[8] == x) or
            (n[0] == x and n[4] == x and n[8] == x) or
            (n[6] == x and n[4] == x and n[2] == x) or
            (n[0] == x and n[3] == x and n[6] == x) or
            (n[1] == x and n[4] == x and n[7] == x) or
            (n[2] == x and n[5] == x and n[8] == x)):
        win = True
        print_field(field)
        if i % 2 == 0:
            print(f'Player {i % 2 + 1} wins!')
        else:
            print('Bot wins')
    return win


def player_turn(message=''):
    if i % 2 == 0:
        turn = list(map(int, input(message).split()))
        x = ' X '
        while len(turn) != 2 or not (3 >= turn[0] >= 1) or not (3 >= turn[1] >= 1):
            turn = list(map(int, input('not acceptable move, please try again: ').split()))
        if turn[0] == 1:
            if field[turn[1] - 1] != ' - ':
                player_turn('such turn has already been made, please try again: ')
            else:
                field[turn[1] - 1] = x
        elif turn[0] == 2:
            if field[turn[1] + 2] != ' - ':
                player_turn('such turn has already been made, please try again: ')
            else:
                field[turn[1] + 2] = x
        else:
            if field[turn[1] + 5] != ' - ':
                player_turn('such turn has already been made, please try again: ')
            else:
                field[turn[1] + 5] = x
    else:
        x = ' 0 '
        turn = [random.randint(1, 3), random.randint(1, 3)]
        if turn[0] == 1:
            if field[turn[1] - 1] != ' - ':
                player_turn()
            else:
                print(f'Bot hits {turn}')
                field[turn[1] - 1] = x
        elif turn[0] == 2:
            if field[turn[1] + 2] != ' - ':
                player_turn()
            else:
                print(f'Bot hits {turn}')
                field[turn[1] + 2] = x
        else:
            if field[turn[1] + 5] != ' - ':
                player_turn()
            else:
                print(f'Bot hits {turn}')
                field[turn[1] + 5] = x
    return x


field = [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
print_field(field)
dice = random.randint(1, 2)
if dice == 1:
    print('Player goes first')
    for i in range(9):
        if win_condition(field, player_turn('please input string and column numbers divided by space: ')):
            break
        else:
            print_field(field)
            print()
        if i == 8:
            print('Draw')
else:
    print('Bot goes first')
    for i in range(1, 10):
        if win_condition(field, player_turn('please input string and column numbers divided by space: ')):
            break
        else:
            print_field(field)
            print()
        if i == 9:
            print('Draw')
