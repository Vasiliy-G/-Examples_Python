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
    # return [random.randint(-100, 101) for _ in range(length + 1)]
    return [-90, 72, 88, -67, -20, 0, -51, 35]

def polynomial_coefficient_list(data):
    polynomial_lst = []
    for coefficient in range(len(data), 0, -1):
        symbol_x, degree, sign = '*x', '^', '+ '
        index_revers = len(data) - coefficient
        coefficient -= 1
        singleton = data[index_revers]

        # убираем *x, ^, коэффицеент на последнем элементе
        if index_revers == len(data)-1 and coefficient == 0:
            symbol_x, degree, coefficient = '', '', ''

        # убираем ^ и коэффицеент на предпоследнем элементе
        elif coefficient == 1:
            degree, coefficient = '', ''

        # убираем знаки перед элементом с нулевым индексом
        # elif index_revers == 0:
        #     sign = ''

        # убираем знак - у отрицательного элемента
        # меняем знак + на - если элемент меньше 0
        if singleton < 0:
            singleton = int(str(singleton).replace('-',''))
            sign = '- '









        print(f'data[index_revers:{index_revers}]: {data[index_revers]}, '
              f'sign: {sign}, '
              f'singleton: {singleton}, '
              f'symbol_x: {symbol_x}, '
              f'degree: {degree}, '
              f'coefficient: {coefficient}')

        res = f'{sign}{singleton}{symbol_x}{degree}{coefficient} '

        # исключаем одночлен с значением 0
        if singleton == 0:
            res = ''

        polynomial_lst.insert(index_revers, res)
    polynomial = f'{"".join(polynomial_lst)}= 0'
    print('data:' ,data)
    print(f'Сформирован список коэффициентов: {polynomial}')
    return polynomial


def main():
    file_write('polynomial.txt', polynomial_coefficient_list(coefficient_rnd_list(random.randint(4, 8))))
    #file_write('polynomial2.txt', polynomial_coefficient_list(coefficient_rnd_list(random.randint(4, 8))))


if __name__ == '__main__':
    main()
