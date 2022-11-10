# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001
#
# !!ВНИМАНИЕ
# # !!! не использовать константу math.pi

from math import asin, sqrt, pi


def number_input(text):
    wh_status = False
    while not wh_status:
        try:
            number = float(input(text))
        except ValueError:
            print('Необходимо ввести дробное число (например: 0.001)')
        else:
            if number <= 0.1 and str(number)[-1] == '1':
                return number
            else:
                print('Необходимо ввести дробное число заканчивающееся на .1)')


def get_pi():
    number_pi = asin(sqrt(1 - 1**2))+ abs(asin(1)) * 2
    #number_pi = pi
    return number_pi


def get_accurate(accurate):
    accurate_len = len(str(accurate).split('.')[1])
    return str(get_pi()).split('.')[1][:accurate_len]


def main():
    print('число π:', get_pi())
    accurate = number_input('Задайте точность вывода числа π (например: 0.001): ')
    to_point = str(get_pi()).split('.')[0]
    after_point = get_accurate(accurate)
    print(f"при d = {accurate}, π = {to_point}.{after_point}")


if __name__ == '__main__':
    main()
