# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11


def numberInput():
    whStatus = False
    while not whStatus:
        number = input(f"Введите вещественное число: ")
        if InputCheck(number):
            whStatus = True
            return number


def InputCheck(number):
    res = False
    for element in number:
        if element.isdigit() or element == '-' or element == '.' or element == ',':
            res = True
    return res


def getSumm(number):
    result = 0
    for element in number.replace('.', '').replace(',', '').replace('-', ''):
        result += int(element)
    return f"{number} -> {result}"


def main():
    print(getSumm(numberInput()))


if __name__ == '__main__':
    main()
