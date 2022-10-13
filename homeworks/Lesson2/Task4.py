# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции вводятся с клавиатуры.

import random


def NumberInput(text, max_num):
    whStatus = False
    while not whStatus:
        try:
            number = int(input(text))
        except ValueError:
            print("Введите число.")
        else:
            if number >= max_num:
                whStatus = True
                return number


def FillNumbersInterval(number):
    numbers_list = []
    for i in range(1, number + 1):
        numbers_list.append(random.randint(-number, number + 1))
    print(f"Список из {number} элементов: {numbers_list}")
    return numbers_list


def ProductPositionElements(numbers_list):
    ## Найдите произведение элементов на указанных позициях.
    # Позиции вводятся с клавиатуры .
    print('Введите позиции элементов для вычисления их произведения')
    position1 = NumberInput("Позиция1: ", 0)
    position2 = NumberInput("Позиция2: ", 0)
    res = numbers_list[position1] * numbers_list[position2]
    print(f'Произведение элементов {numbers_list[position1]} и '
          f'{numbers_list[position2]} = {res}')


def main():
    numbers_list = FillNumbersInterval(NumberInput('Введите число N (не меньше 2х): ', 2))
    for i in range(len(numbers_list)):
        print('позиция:', i, 'элемент:', numbers_list[i])
    ProductPositionElements(numbers_list)


if __name__ == '__main__':
    main()
