# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
#
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


def coordinatesInput(namesList):
    coordinatesList = []

    for i in range(len(namesList)):
        whStatus = False
        while not whStatus:
            try:
                coordinate = int(input(f"Введите координаты {namesList[i]}: "))
            except ValueError:
                print("Введите число.")
            else:
                if coordinate == 0:
                    print("координаты не могут равнятся нулю.")
                else:
                    coordinatesList.append(coordinate)
                    whStatus = True
    return coordinatesList


def coordinatesCheck(coordinatesList):
    x = coordinatesList[0]
    y = coordinatesList[1]
    result = "IV"
    if x > 0 and y > 0:
        result = "I"
    elif x < 0 and y > 0:
        result = "II"
    elif x < 0 and y < 0:
        result = "III"
    print(f"X={x}; Y={y} -> {result} четверть плоскости.")


def main():
    namesList = ("X", "Y")
    coordinatesCheck(coordinatesInput(namesList))


if __name__ == '__main__':
    main()

