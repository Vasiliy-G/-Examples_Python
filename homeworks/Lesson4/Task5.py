# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0
#
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0

import re
import Task4


def file_read(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data


def check_match(polynomials_sum_list, degree):
    res = True
    for match in polynomials_sum_list:
        if degree[1] == match[1]:
            res = False
    return res


def singleton_extraction(filename):
    polynomial = file_read(filename)
    element_list = polynomial.split(' ')
    index = 2
    polynomial_list_clear =[]

    # создаем список с нулевым элементом
    polynomial_list = [re.findall('[-+]?[\d\w]+', element_list[0])]
    while(index < len(element_list)-2):

        # манипуляции с арифметическими знаками
        sign_arithmetic = ''
        if element_list[index -1] == '-':
            sign_arithmetic = '-'
        res = re.findall('[-+]?[\d\w]+', element_list[index])
        res[0] = sign_arithmetic+res[0]#.replace('x', '')

        # добавляем степень в предпоследний и последний одночлен
        if len(res) == 1:
            if 'x' in str(res):
                res.append('1')
            else:
                res.append('0')
        polynomial_list.append(res)
        index += 2

    # очищаем список от x
    for i in polynomial_list:
        find_digit = re.search('[-+]?[\d\w]+', i[0]).group()
        i[0] = str(find_digit).replace('x', '')

        if (len(i[0]) == 0 or len(i[0]) == 1) and ('' in i[0] or '-' in i[0]):
            i[0] = i[0] + '1'

        polynomial_list_clear.append([int(i[0]), int(i[1])])
    return polynomial_list_clear


def get_polynomials_sum(polynomial1, polynomial2):
    res1, res2, res3 = '', '', ''
    degree_list = []
    polynomials_sum_list = []
    polynomial_max = polynomial1
    polynomial_min = polynomial2

    if (polynomial_max[0][1] < polynomial_min[0][1]) or (len(polynomial_max) < len(polynomial_min)):
        polynomial_max = polynomial2
        polynomial_min = polynomial1

    for i in range(len(polynomial_max)):
        degree_list.append(polynomial_max[i][1])
    for j in range(len(polynomial_min)):
        degree_list.append(polynomial_min[j][1])

    degree_list = list(set(degree_list))
    degree_list.sort(reverse=True)

    for degree in degree_list:
        for i in range(len(polynomial_max)):
            for j in range(len(polynomial_min)):
                if polynomial_max[i][1] == degree and polynomial_max[i][1] == polynomial_min[j][1]:
                    polynomials_sum_list.append([polynomial_max[i][0] + polynomial_min[j][0], degree])

                elif check_match(polynomial_min, polynomial_max[i]) \
                    and polynomial_max[i] not in polynomials_sum_list \
                    and polynomial_max[i][1] == degree:
                        res2 = polynomial_max[i]

                elif check_match(polynomial_max, polynomial_min[j]) \
                    and polynomial_min[j] not in polynomials_sum_list \
                    and polynomial_min[j][1] == degree:
                        res3 = polynomial_min[j]

            if res2:
                polynomials_sum_list.append(res2)
            if res3:
                polynomials_sum_list.append(res3)

            res1, res2, res3 = '', '', ''

    return polynomials_sum_list


def main():
    filenames = Task4.main()
    filename = filenames[0].split('.')
    filename = filename[0] + '_sum.' + filename[1]

    polynomial1 = singleton_extraction(filenames[0])
    polynomial2 = singleton_extraction(filenames[1])

    polynomials_sum_lst = get_polynomials_sum(polynomial1, polynomial2)

    polynomials_sum = Task4.polynomial_build(polynomials_sum_lst)

    print('\nСумма многочлена:', polynomials_sum)

    Task4.file_write(filename, polynomials_sum)


if __name__ == '__main__':
    main()
