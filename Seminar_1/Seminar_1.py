'''1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
    *Примеры:* 
    - 5, 25 -> да
    - 4, 16 -> да
    - 25, 5 -> да
    - 8,9 -> нет
2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    Примеры:
    - 1, 4, 8, 7, 5 -> 8
    - 78, 55, 36, 90, 2 -> 90
'''
def degree():
    firstNumber = int(input("Введите число 1"))
    secondNumber = int(input("Введите число 2"))
    if firstNumber**2 == secondNumber:
        print("firstNumber является квадратом числа secondNumber")
    else:
        print("firstNumber не является квадратом числа secondNuber")

def numberArray():
    listNumber = []
    for _ in range(5):
        number = int(input("введите число: "))
        listNumber.append(number)
    maxNumber = listNumber[0]
    for num in listNumber:
        if num > maxNumber:
            maxNumber = num
    return maxNumber

'''
1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
    *Примеры:* 
    
    - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    *Примеры:*
    - 6,78 -> 7
    - 5 -> нет
    - 0,34 -> 3
3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
'''
def task_1():
    number = int(input("Введите число: "))
    for i in range( -number, number + 1 ):
        print(i, end=" ")

def task_2():
    fraction = float(input("Введите число:"))
    print(int(fraction%1 * 10))

def task_3():
    number = int(input())
    if (number%5 == 0 and number%10 == 0 and number%30 != 0) or (number%15 == 0 and number%30 != 0):
        print("Число удовлетворяет условию:")
    else:
        print("Число не кратно ")