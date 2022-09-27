#задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#и проверяет, является ли этот день выходным.

def get_int(): # Запрашивает консольный ввод пока не будет введено целое число
    number = None
    while ValueError:
        try:
            number = int(input("Введите целое число: "))
            return number
        except ValueError:
            print("Вы ввели не целое число, повторите ввод: ")
        
def day_week(): # Задача 1. День недели
    number = get_int()
    while number < 1 or number > 7:
        print("Такого дня недели нет, повторите ввод: ")
        number = get_int()

    day = number
    if day <= 5:
        print("Этот день рабочий")
    else:
        print("Этот день выходной!")

# задача 2. Напишите программу для.
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


import random
def predicatives(quantity = 3): # Генерирует массив случайных высказываний к задаче 2
    seq = [True, False]
    result = []
    for _ in range(0, quantity):
        result.append(bool(random.choice(seq)))
    return result

def conjunction(arr = []): # Задача 2. Проверяет истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
    conjunction = not (arr[0] and arr[1] and arr[2])
    disjunction = not arr[0] or not arr[1] or not arr[2]
    result = conjunction == disjunction
    
    print(f'''  результат первого высказывания: {conjunction}, 
                результат второго высказывания: {disjunction}, 
                результат сравнения высказываний: {result}''')

'''
задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
*Пример:*
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''
def point_coordinat(): # Задача 3. Принимает координаты точки
    coord_x = 0
    coord_y = 0
    while coord_x == 0 or coord_y == 0:
        coord_x = get_int()
        coord_y = get_int()
        if coord_x < 0 and coord_y > 0:
            print("Точка находится в 1 четверти!")
        elif coord_x > 0 and coord_y > 0:
            print("Точка находится в 2 четверти!")
        elif coord_x > 0 and coord_y < 0:
            print("Точка находится в 3 четверти!")
        elif coord_x < 0 and coord_y < 0:
            print("Точка находится в 4 четверти!")
        else:
            print("Вы ввели 0, повторите ввод: ")

'''
задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.
Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
Обратите внимание, что на вход программе приходят вещественные числа.
'''

def get_float(): # Запрашивает консольный ввод пока не будет введено вещественное число
    number = None
    while ValueError:
        try:
            number = float(input("Введите вещественное число: "))
            return number
        except ValueError:
            print("Вы ввели не вещественное число, повторите ввод: ")

def calc(): # Задача 4. Калькулятор
    first_number = get_float()
    second_number = get_float()
    result = None
    operation = None
    while (
        operation != "+" or
        operation != "-" or
        operation != "/" or
        operation != "*" or
        operation != "mod" or
        operation != "pow" or
        operation != "div"):
        print('''
    Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.
    ''')
        try:
            operation = input("Введите операцию: ").lower()
            if operation == "+":
                result = first_number + second_number
            elif operation == "-":
                result = first_number - second_number
            elif operation == "/":
                result = first_number / second_number
            elif operation == "*":
                result = first_number * second_number
            elif operation == "%":
                result = first_number % second_number
            elif operation == "pow":
                result = first_number ** second_number
            elif operation == "div":
                result = first_number // second_number
            print(f" {first_number} {operation} {second_number} = {result} ")
            break
        except ZeroDivisionError:
            print("Деление на 0!")
            break

'''
Задача 5 VERY HARD SORT необязательная
Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
Отсортировать элементы по возрастанию слева направо и сверху вниз.
'''

def get_sequence(): # Создает матрицу, заполненную случайными значениями
    print("Введите число строк матреци: ")
    rows = get_int()
    print("Введите число колонок матреци: ")
    columns = get_int()
    print("Введите минемальное значение элемента матреци: ")
    min = get_int()
    print("Введите максимальное значение элемента матреци: ")
    max = get_int()
    seq =[[0] * rows for _ in range(columns)]
    for i in range(len(seq)):
        for j in range(len(seq[i])):
            seq[i][j] = random.randint(min, max)  
    return seq

def sorting_matrix(arr = []): # Сортирует каждую строку матрици а затем сортирует матрици
    first_seq = []
    second_seq = []
    for i in arr:   
        second_seq.append(sorted(i))        
    first_seq = sorted(second_seq)  
    return first_seq

def sorting_full_matrix(arr = []): # Сортирует все элементы матреци 
    first_seq = []
    for i in arr:
        for j in i:
            first_seq.append(j)
    second_seq = sorted(first_seq)
    third_seq = [[None] * len(arr) for _ in range(len(arr[0]))]
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            third_seq[i][j] = second_seq[0]
            second_seq.remove(second_seq[0])
    return third_seq
    
def output_matrix(arr = []): # Выводит массив на печать
    print("[")
    for i in arr:
        print(f"    {i} ")
    print("]")

def menu(): # Функция меню для удобного перехода к нужной задаче
    menu = ["1", "2", "3", "4", "5","6", "0"]
    point = None
    while point not in menu:
        print('''
        1 - задача 1 День недели
        2 - задача 2 Проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
        3 - задача 3 Номер четверти плоскости, по введеннвм координатам
        4 - задача 4 Калькулятор (консольный)
        5 - задача 5 Сортировка матреци сначало элементы строки за тем массивы
        6 - задача 5 Сортировка всех элементов матрици по возростанию
        0 - Выход 
        ''')
        point = input("Введите, интерисующий пункт меню: ")

        if point == "1": day_week()
        if point == "2": conjunction(predicatives())
        if point == "3": point_coordinat()
        if point == "4": calc()
        if point == "5": output_matrix(sorting_matrix(get_sequence()))
        if point == "6": output_matrix(sorting_full_matrix(get_sequence()))
        if point == "0": break

menu()