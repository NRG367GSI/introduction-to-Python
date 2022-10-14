#Создание списка кортежей число и его квадрат
list_1 = [(i, i**2) for i in range(1,21) if i%2==0 ]
print(list_1)

def f(x):
    return x**3
#Создание списка кортежей из числа и значения возрощенного функциеей по принятому значению из итератора с условием
list_2 = [(i, f(i)) for i in range(1,21) if i%2 == 0]
print(list_2)

# Тоже самое с лябдой
f = lambda i: i**3
list_3 = [(i, f(i) ) for i in range(1,21) if i%2 == 0]
print(list_3)

path = 'C:/Users/Professional/Desktop/Python_exp/introduction to Python/lecture_3_and/number.txt'
f = open(path, 'r')
data = f.read(1)
print(data)
f.close()

