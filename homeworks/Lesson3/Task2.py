# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random


def NumberInput(text):
    whStatus = False
    while not whStatus:
        try:
            number = int(input(text))
        except ValueError:
            print("Введите число.")
        else:
            return number


def NumbersListFill(number):
    return [random.randint(1, 11) for i in range(number)]


def ProductPairsNumbers(numbers_list):
    len_nl = int(len(numbers_list)/2) + 1
    if len(numbers_list) % 2 == 0:
        len_nl = int(len(numbers_list)/2)
    return [numbers_list[i] * numbers_list[(i*(-1))-1] for i in range(0, len_nl, 1)]


def main():
    numbers_list = NumbersListFill(NumberInput('Введите размер списка: '))
    res_list = ProductPairsNumbers(numbers_list)
    print(f'{numbers_list} => {res_list}')


if __name__ == '__main__':
    main()
