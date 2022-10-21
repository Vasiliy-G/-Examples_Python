# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

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
    return [random.randint(100, 1001) / 100.0 for _ in range(number)]


def DiffMaxMinValues(numbers_list):
    val_max = str(numbers_list[0]).split('.')[1]
    val_min = str(numbers_list[0]).split('.')[1]
    for i in range(1, len(numbers_list)):
        if str(numbers_list[i]).split('.')[1] > val_max:
            val_max = str(numbers_list[i]).split('.')[1]
        elif str(numbers_list[i]).split('.')[1] < val_min:
            val_min = str(numbers_list[i]).split('.')[1]
    # print('val_max=', val_max, '\nval_min=', val_min)
    return int(val_max) - int(val_min)


def main():
    numbers_list = NumbersListFill(NumberInput('Введите размер списка: '))
    res = (DiffMaxMinValues(numbers_list))
    print(f'{numbers_list} => {res}')


if __name__ == '__main__':
    main()
