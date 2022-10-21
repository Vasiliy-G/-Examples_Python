# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def number_input(text):
    whStatus = False
    while not whStatus:
        try:
            number = int(input(text))
        except ValueError:
            print("Введите число.")
        else:
            return number


def fibonacci(n):
    fibonacci_list = []
    a, b = 1, 1
    for _ in range(n):
        fibonacci_list.append(a)
        a, b = b, a + b
    return fibonacci_list


def negafibonacci(n):
    negafibonacci_list = []
    a, b = 0, 1
    for _ in range(n + 1):
        negafibonacci_list.insert(0, a)
        a, b = b, a - b
    return negafibonacci_list


def main():
    number = number_input('Введите число: ')
    print(negafibonacci(number) + fibonacci(number))

if __name__ == '__main__':
    main()
