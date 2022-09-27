'''
10. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в
2D пространстве.
    
    *Пример:*
    
    - A (3,6); B (2,1) -> 5,09
    - A (7,-5); B (1,-1) -> 7,21

11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
    *Пример:*
    
    - Для N = 5: 1, -3, 9, -27, 81

'''

def get_int(): # Запрашивает консольный ввод пока не будет введено целое число
    number = None
    while ValueError:
        try:
            number = int(input("Введите целое число: "))
            return number
        except ValueError:
            print("Вы ввели не целое число, повторите ввод: ")

import math
def decard():
    print("Введите координаты точки А: ")
    a_x = get_int()
    print("Введите координаты точки И: ")
    a_y = get_int()
    b_x = get_int()
    b_y = get_int()
    distance = round(math.sqrt((a_x - b_x)**2 + (a_y - b_y)**2), 3)
    print(distance)
#decard()

def quanty():
    number = get_int()
    for i in range(0, number + 1):
        print(i)

#quanty()

def decard_n():
    print("Введите колличество измерений пространства: ")
    num = get_int()
    dec_a = [None] * num
    dec_b = [None] * num
    for i in range(0, num - 1):
        print(f"Введите координату {i} ")
        dec_a[i] = get_int()
        dec_b[i] = get_int()
    summ = None
    for j in range(0, num - 1):
        distance = dec_a[j]**2 - dec_b[j]**2
        summ += distance
    result = math.sqrt(summ)
    print(result)

'''
12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
    *Пример:*
    
    - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
13. Напишите программу, в которой пользователь будет задавать две строки, 
а программа - определять количество вхождений одной строки в другой.

'''

def dictionare():
    print("Колличество элементов словоря: ")
    number = get_int()
    dict = {}
    for i in range(1, number + 1):
        dict[i] = 3 * i + 1
    print(dict)

def dictionare_2():
    str_1 = input("Введите 1 строку: ")
    str_2 = input("Введите 2 строку: ")
    count = 0
    for i in str_1:
        if i == str_2:
            count += 1
    print(count)

dictionare()

