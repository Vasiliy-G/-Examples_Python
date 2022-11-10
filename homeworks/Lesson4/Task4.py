# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от -100 до 100) многочлена
# и записать в файл многочлен степени k

# k - максимальная степень многочлена,
# следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random,
# поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Записываем результат в файл.
#
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random


def file_write(filename, data):
    with open(filename, 'w') as file:
        file.write(data)


def coefficient_rnd_list(length):
    return [random.randint(-100, 101) for _ in range(length + 1)]


def polynomial_coefficient_list(data):
    #print(f'\ndata: {data}; len: {len(data)-1}')
    polynomial_lst = []
    for degree in range(len(data), 0, -1):
        index = len(data) - degree
        degree -= 1
        coefficient = data[index]
        res = [coefficient, degree]
        if coefficient != 0:
            polynomial_lst.append(res)
    #print('polynomial_lst:', polynomial_lst)
    return polynomial_lst


def polynomial_build(polynomial_lst):
    polynomial_lst_build = []
    symbol_x, sign_degree, sign_arithmetic = 'x', '^', ''
    for position, value in enumerate(polynomial_lst):
        coefficient = int(value[0])
        degree = int(value[1])

        # манипуляции с арифметическими знаками
        if coefficient < 0 and position != 0:
            sign_arithmetic = ' - '
            coefficient *= -1
        elif coefficient >= 0 and position != 0:
            sign_arithmetic = ' + '
        else:
            sign_arithmetic = ''

        # убираем x, ^, '+', коэффицеент на последнем элементе многочлена
        if degree == 0:
            symbol_x, sign_degree, degree = '', '', ''

        # убираем ^ и коэффицеент на предпоследнем элементе многочлена
        elif degree == 1:
            sign_degree, degree = '', ''

        # манипуляции с множителем x и первым элементом многочлена
        #if (coefficient == 1 or coefficient == -1) and (symbol_x == 'x' and position != 0):

        if position == 0 and coefficient == -1:
            coefficient = '-'
        elif (coefficient == 1 or coefficient == -1) and (symbol_x == 'x'):
            coefficient = ''

        res = f'{sign_arithmetic}{coefficient}{symbol_x}{sign_degree}{degree}'
        polynomial_lst_build.append(res)

    polynomial_build = ''.join(polynomial_lst_build) + ' = 0'
    return polynomial_build


def main():
    filename = 'polynomial.txt'
    filename2 = 'polynomial2.txt'

    polynomial_lst1 = polynomial_coefficient_list(coefficient_rnd_list(random.randint(4, 8)))
    polynomial_lst2 = polynomial_coefficient_list(coefficient_rnd_list(random.randint(4, 8)))

    polynomial1 = polynomial_build(polynomial_lst1)
    polynomial2 = polynomial_build(polynomial_lst2)

    print(f'Сформирован список коэффициентов: {polynomial1}')
    print(f'Сформирован список коэффициентов: {polynomial2}')

    file_write(filename, polynomial1)
    file_write(filename2, polynomial2)

    return filename, filename2


if __name__ == '__main__':
    main()
