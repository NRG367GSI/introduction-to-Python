#Задача 1 Сумма чисел введенного числа

def get_float(): # Запрашивает консольный ввод пока не будет введено вещественное число
    number = None
    while ValueError:
        try:
            number = float(input("Введите вещественное число: "))
            return number
        except ValueError:
            print("Вы ввели не вещественное число, повторите ввод: ")

def sum_number_entered(): # Без дополнительных модулей Python
    summ = 0
    number = 0
    number = get_float()
    if number < 0:
        number = -1 * number
    while round(number, 5) % 1 != 0:
        number *= 10
    while number != 0:
        summ += int(number % 10)
        number = int(number / 10)
    print(summ)
    input("Нажмите Enter для выхода: ")
    menu()

# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def get_int(): # Запрашивает консольный ввод пока не будет введено целое число
    number = None
    while ValueError:
        try:
            number = int(input("Введите целое число: "))
            return number
        except ValueError:
            print("Вы ввели не целое число, повторите ввод: ")

def factorial():
    result = 1
    number = get_int()
    for i in range(1, number + 1):
        result *= i
        print(result)
    input("Нажмите Enter для выхода: ")
    menu()

# Задача 3. Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами,
# выводится на экран, затем перемешивается, опять выводится на экран.

def random_sequence(): # Генерирует список из случайных целых значений
    from random import randrange
    print("min: ")
    min = get_int()
    print("max: ")
    max = get_int()
    print("size: ")
    size = get_int()
    seq = []
    while len(seq) < size:
        i = randrange(min, max)
        seq.append(i)
    return seq

def mix_sequence(arr = []): # Алгоритм перемешивания списка
    seq = [] * len(arr)
    print(arr)
    while len(arr) != 0:
        if len(arr)%2 != 0:
            seq.append(arr[int(len(arr)/2)])
            arr.pop(int(len(arr)/2))
        elif len(arr) != 0:
            seq.append(arr[-1])
            arr.pop(-1)
            if arr[0] != seq[-1]:
                seq.append(arr[0])
                arr.pop(0)
            else: continue
    print(seq)
    input("Нажмите Enter для выхода: ")
    menu()


# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N,
# и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

def decard_n(): # Принемает координаты 2-х точек и находит расстояние между ними
    print("Введите колличество измерений пространства: ")
    num = get_int()
    dec_a = [None] * num
    dec_b = [None] * num
    for i in range(0, num - 1):
        print(f"Введите координату {i} ")
        dec_a[i] = get_int()
        dec_b[i] = get_int()
    summ = 0
    for j in range(0, num - 1):
        distance = (dec_a[j] - dec_b[j])**2
        summ += distance
    result = summ**(1/2)
    print(result)


# Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат. Количество предикатов генерируется случайным образом от 5 до 11, проверяем это
# утверждение 10 раз, с помощью модуля time выводим на экран , сколько времени отработала программа.

def predicatives(): # Генерирует массив случайных высказываний к задаче 2
    import random
    seq = [True, False]
    result = []
    for _ in range(0, random.randint(5, 11)):
        result.append(bool(random.choice(seq)))
    return result

def conjunction(arr = []): # Задача 5. Проверяет истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
    mult = bool(None)
    disjunction = bool(None)
    for i in arr:
        mult = mult and arr[i]
        disjunction = disjunction or not arr[i]
    conjunction = not mult
    result = conjunction == disjunction
    print(f'''  
                предикат: {arr}
                результат первого высказывания: {conjunction}, 
                результат второго высказывания: {disjunction}, 
                результат сравнения высказываний: {result}''')
    input("Нажмите Enter для выхода: ")
    menu()

def menu(): # Функция меню для удобного перехода к нужной задаче
    menu = ["1", "2", "3", "4", "5", "0"]
    point = None
    while point not in menu:
        print('''
        1 - задача 1 Сумма чисел введенного числа (Без дополнительных модулей Python)
        2 - задача 2 Принимает на вход число N и выдает набор произведений чисел от 1 до N.
        3 - задача 3 Алгоритм перемешивания списка
        4 - задача 4 Принимает координаты двух точек и находит расстояние между ними в N-мерном пространстве.
        5 - задача 5 Проверяет истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
        0 - Выход 
        ''')
        point = input("Введите, интерисующий пункт меню: ")

        if point == "1": sum_number_entered()
        if point == "2": factorial()
        if point == "3": mix_sequence(random_sequence())
        if point == "4": decard_n()
        if point == "5": conjunction(predicatives())
        if point == "0": break

menu()