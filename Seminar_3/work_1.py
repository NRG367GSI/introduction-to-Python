'''
16. Задайте список из n чисел последовательности (1 + 1/n)*n  и выведите на экран их сумму.
17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

'''

from unittest import result


def sequence(size): 
    
    seq = [0] * size
    summ = 0
    for i in range(size):
        seq[i] = round((1 + 1/(i + 1))**i, 2)
        summ += seq[i]
    return summ

'''  
try:
    print(sequence(10))
except: print("Произошла ошибка!")
'''

def task_17():
    n = int(input("Введите деапазон значений: "))
    data = open('file.txt', 'r')
    for j in data:
        print(j)
    seq = []
    for i in range(-n, n):
        seq.append(i)
    print(seq)

'''
20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
*Пример:*
- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1
'''

seq =["uhbnsfdhu", "ij8", "jsj", "10"]

def sequence(number, seq):
    result = False
    
    for i in seq:
        if str(number) in i: 
            result = True
            break
    return result
    
print(sequence(8, seq))
'''
def task_21(seq, val):
    count = 0
    for i in seq:
        if str(val) in i:
'''