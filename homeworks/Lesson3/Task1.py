# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


def NumbersListFill(number):
    return [random.randint(1, 11) for _ in range(number)]


def OddItemsFind(numbers_list):
    return [numbers_list[i] for i in range(1, len(numbers_list), 2)]


def main():
    numbers_list = NumbersListFill(5)
    odd_items = ' и '.join(map(str, OddItemsFind(numbers_list)))
    odd_items_summ = sum(OddItemsFind(numbers_list))
    print(f'{numbers_list} -> на нечётных позициях элементы {odd_items},'
          f' ответ: {odd_items_summ}')


if __name__ == '__main__':
    main()
