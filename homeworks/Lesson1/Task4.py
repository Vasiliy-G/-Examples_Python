# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

import random


def numberInput():
    whStatus = False
    while not whStatus:
        quarter = random.randint(1, 4)
        try:
            number = int(input(f"Введите номер четверти (например {quarter}): "))
        except ValueError:
            print("Введите число от 1 до 4.")
        else:
            if 4 < number or number < 1:
                print("Введите число от 1 до 4.")
            else:
                whStatus = True
                return number


def main():
    coordinates_list = ["x = [0; +бесконечность]; y = [0; +бесконечность]",
                        "x = [0; -бесконечность]; y = [0; +бесконечность]",
                        "x = [0; -бесконечность]; y = [0; -бесконечность]",
                        "x = [0; бесконечность]; y = [0; -бесконечность]"]
    print(coordinates_list[numberInput() - 1])


if __name__ == '__main__':
    main()
