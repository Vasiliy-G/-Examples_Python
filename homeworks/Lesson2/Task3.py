# Задайте список из n чисел последовательности (1 + 1/n)^n
# и выведите на экран их сумму.
# *Пример:*
#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

import math


def numberInput():
    whStatus = False
    while not whStatus:
        try:
            number = int(input(f"Введите число N: "))
        except ValueError:
            print("Введите число.")
        else:
            whStatus = True
            return number


def sequencesNumbers(number):
    sequences_numbers_dict = {}
    sum = 0
    for i in range(1, number + 1):
        #res = (1 + 1 / i) ** i
        res = math.pow(1 + 1 / i, i) # math. pow()
        sequences_numbers_dict[i] = float(format(res, '.2f'))
        sum += res
    print(f"Для n={number} {sequences_numbers_dict} \nСумма: {format(sum, '.2f')}")


def main():
    sequencesNumbers(numberInput())


if __name__ == '__main__':
    main()
