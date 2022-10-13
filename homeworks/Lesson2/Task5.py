#  Реализуйте алгоритм перемешивания списка.

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


def NumbersRandom(quantitie):
    return random.randint(0, quantitie)


def NumbersListFill(number):
    numbers_list = []
    for i in range(number):
        numbers_list.append(NumbersRandom(100))
    print(f"Список из {number} элементов: {numbers_list}")
    return numbers_list


def NumbersListMix(numbers_list):
    numbers_list_mix_index = []
    numbers_list_mix = []
    i = 0
    while i < len(numbers_list):
        numbers_rnd = NumbersRandom(len(numbers_list)-1)
        if numbers_rnd not in numbers_list_mix_index:
            numbers_list_mix_index.append(numbers_rnd)
            i = i + 1
    for i in numbers_list_mix_index:
        numbers_list_mix.append(numbers_list[i])
    return numbers_list_mix


def main():
    numbers_list = NumbersListFill(NumberInput('Введите размер списка: '))
    print(f'Перемешанный список: {NumbersListMix(numbers_list)}')


if __name__ == '__main__':
    main()
