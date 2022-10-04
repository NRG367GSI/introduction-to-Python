'''
from fractions import Fraction 
a = Fraction(1)/Fraction(3)
print(a)
'''

'''
26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    *Пример:*
    - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
F n = F n − 1 + F n

F−1 = 1,
F−2 = -1,
Fn = F(n+2)−F(n+1).
'''
'''
def fibonaci(number):
    if number in [1,2]: return 1
    else: return fibonaci (number-1) + fibonaci (number-2)

list = []
for e in range(1, 10):
    list.append(fibonaci(e))
print(list)

Отношения к нормальной, положительной последовательности чисел Фибоначчи:

{\displaystyle F(-n)=(-1)^{n+1}\cdot F(n)}{\displaystyle F(-n)=(-1)^{n+1}\cdot F(n)}

'''

'''
28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
    1) с помощью математических формул нахождения корней квадратного уравнения
    
    2) с помощью дополнительных библиотек Python
    
29. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

'''
def least_multiple(a, b):
    for number in range(2, b):
        if a%number == 0 and b%number == 0:
            print(number)
            break

least_multiple(30, 120)




