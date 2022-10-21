# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def NumberInput(text):
    whStatus = False
    while not whStatus:
        try:
            number = int(input(text))
        except ValueError:
            print("Введите число.")
        else:
            return number


def ConvertDecToBin(x):
        return (str(bin(x)).replace('0b', ''))


def ConvertDecToBin2(n):
    if(n > 1):
        ConvertDecToBin2(n//2)
    print(n%2, end='')


def ConvertDecToBin3(numbers):
    bin_list=[]
    while (numbers > 0):
        bin_list.append(str(numbers%2))
        numbers //= 2
    bin_list.reverse()
    return (''.join(bin_list))


def main():
    numbers = NumberInput('Введите число: ')

    # Вариант1
    print(f'{numbers} -> {ConvertDecToBin(numbers)}')

    # Вариант2
    print(numbers, '-> ', end='')
    ConvertDecToBin2(numbers)

    # Вариант3
    print(f'\n{numbers} -> {ConvertDecToBin3(numbers)}')


if __name__ == '__main__':
    main()




