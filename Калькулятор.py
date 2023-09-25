import math

def calculator():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("11. Выход")

    operation = input("Введите номер операции:")
    if operation in ('1', '2', '3', '4','5'):
        while True:
            try:
                number1 = int(input("Введите первое число: "))
                number2 = int(input("Введите второе число: "))
                break
            except ValueError:
                print("Invalid")
    elif operation in ('6','7','8','9','10'):
        while True:
            try:
                number= int(input("Введите число: "))
                break
            except ValueError:
                print("Invalid")
    else:

        if operation == "11":
         print("Бай бай")
        return

    if operation == '1':
        result = number1 + number2
        print("Результат: ", result)

    elif operation == '2':
        result = number1 - number2
        print("Результат: ", result)

    elif operation == '3':
        result = number1 * number2
        print("Результат: ", result)

    elif operation == '4':
        if number2 == 0:
            print("Ошибка: деление на 0 недопустимо")
        else:
            result = number1 / number2
            print("Результат: ", result)

    elif operation == '5':

        result = number1 ** number2
        print("Результат: ", result)

    elif operation == '6':

        if number < 0:
            print("Ошибка: квадратный корень из отрицательного числа недопустим")
        else:
            result = math.sqrt(number)
            print("Результат: ", result)

    elif operation == '7':
        if number< 0:
            print("Ошибка: факториал отрицательного числа недопустим")
        else:
            result = math.factorial(number)
            print("Результат: ", result)

    elif operation == '8':

        result = math.sin(math.radians(number))
        print("Результат: ", result)

    elif operation == '9':

        result = math.cos(math.radians(number))
        print("Результат: ", result)

    elif operation == '10':

        result = math.tan(math.radians(number))
        print("Результат: ", result)

    else:
        print("Ошибка: некорректный номер операции")

    print("\n")
    calculator()


calculator()
