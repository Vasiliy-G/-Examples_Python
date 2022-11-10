# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.


def number_input(text):
    wh_status = False
    while not wh_status:
        try:
            number = int(input(text))
        except ValueError:
            print('Необходимо ввести число!')
        else:
            return number


def factoring_integers(num):
    simple_number = 2
    factoring_lst = []
    while simple_number <= num:
        if num % simple_number == 0:
            factoring_lst.append(simple_number)
            num //= simple_number
            simple_number = 2
        else:
            simple_number += 1
    return factoring_lst


def main():
    number = number_input('Задайте натуральное число (например 360): ')
    print(f'Список простых множителей числа {number}: {factoring_integers(number)}')


if __name__ == '__main__':
    main()
