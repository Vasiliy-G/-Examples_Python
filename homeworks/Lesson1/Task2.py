# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def numberInput(namesList):
    numberList = []
    for i in range(len(namesList)):
        whStatus = False
        while not whStatus:
            try:
                number = int(input(f"Введите значение {namesList[i]}: "))
            except ValueError:
                print("Введите число.")
            else:
                numberList.append(number)
                whStatus = True
    return numberList


def is_predicate(numberList):
    x = numberList[0]
    y = numberList[1]
    z = numberList[2]

    left = not (x or y or z)
    right = not x and not y and not z
    if left == right:
        print("Утверждение истинно.")
    else:
        print("Утверждение ложно.")


def main():
    namesList = ("X", "Y", "Z")
    is_predicate(numberInput(namesList))


if __name__ == '__main__':
    main()
