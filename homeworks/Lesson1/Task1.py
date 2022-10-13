# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

import random


def numberInput():
    whStatus = False
    while not whStatus:
        weekday = random.randint(1, 7)
        try:
            number = int(input(f"Введите номер дня недели (например {weekday}): "))
        except ValueError:
            print("Введите число от 1 до 7.")
        else:
            if 7 < number or number < 1:
                print("Введите число от 1 до 7.")
            else:
                whStatus = True
                return number


def numberCheck(number):
    res = "нет"
    if number == 6 or number == 7:
        res = "да"
    print(f"{number} -> {res}")


def main():
    numberCheck(numberInput())

if __name__ == '__main__':
    main()
