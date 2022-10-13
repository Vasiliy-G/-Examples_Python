# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import random
import math


def coordinate_random():
    return random.randint(-10, 11)


def coordinatesInput(namesList):
    coordinatesList = []
    for i in range(len(namesList)):
        whStatus = False
        while not whStatus:
            coordinate = (input(f"Введите координаты X Y точки {namesList[i]}"
                                f" через пробел (например {coordinate_random()}"
                                f" {coordinate_random()}): ")).split()
            if not InputCheck(coordinate, namesList):
                print('Ошибка ввода координат, повторите ввод.')
            else:
                print(f'Координаты точки {namesList[i]}: X={coordinate[0]}; Y={coordinate[1]}')
                coordinatesList.append(coordinate)
                whStatus = True
    return coordinatesList


def InputCheck(coordinate, namesList):
    res = False
    for element in coordinate:
        if element.isdigit() and len(coordinate) == len(namesList):
            res = True
    return res


def pointSpacing(coordinates):
    p1 = coordinates[0]
    p2 = coordinates[1]
    return math.sqrt(((int(p1[0]) - int(p2[0])) ** 2) + ((int(p1[1]) - int(p2[1])) ** 2))


def main():
    namesList = ("A", "B")
    res = pointSpacing(coordinatesInput(namesList))
    print(f"Расстояние между точками {namesList[0]} и {namesList[1]}: {format(res, '.2f')}")


if __name__ == '__main__':
    main()
