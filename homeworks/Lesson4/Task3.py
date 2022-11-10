# Задайте последовательность цифр. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


def number_input(text):
    wh_status = False
    while not wh_status:
        try:
            digits = int(input(text))
        except ValueError:
            print('Необходимо ввести числа (например: 1113384455229)')
        else:
            return digits


def nonrepeating_elements(elements):
    nonrepeating_elements_list = []
    for element in str(elements):
        if str(elements).count(element) == 1:
            nonrepeating_elements_list.append(int(element))
    return nonrepeating_elements_list


def main():
    digits = number_input('Задайте последовательность цифр (например: 1113384455229): ')
    print(f'{digits} -> {nonrepeating_elements(digits)}')


if __name__ == '__main__':
    main()
