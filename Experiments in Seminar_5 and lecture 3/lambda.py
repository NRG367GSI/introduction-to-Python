# map() применяет функцию к списку для вывода списка требуется list
'''
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(squared) # [1, 4, 9, 16, 25]

def square(number):
    return number ** 2
numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)
print(list(squared)) #[1, 4, 9, 16, 25]
print(list("Строка")) # Результат список элементов: ['С', 'т', 'р', 'о', 'к', 'а']
'''
#filter() применяет функцию условие к списку для вывода списка требуется list
# список чисел
'''
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

# функция, которая проверяет числа
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

'''
# Применение filter() для удаления нечетных чисел
'''
out_filter = filter(filter_odd_num, numbers)

print("Тип объекта out_filter: ", type(out_filter))
print("Отфильтрованный список: ", list(out_filter))
'''

#zip() функция берет на вход несколько списков и создает список кортежей по индексу списков 0 - 0, 1-1 и тд.
'''
s = 'abc'
t = (10, 20, 30)
u = (-5, -10, -15)

print(list(zip(s,t,u))) #[('a', 10, -5), ('b', 20, -10), ('c', 30, -15)]
'''
# интовые значения введенные через пробел преабразуется в список чисел
'''
data = list(map(int, input("введите: ").split())) 
print(data)
'''

# Если range() позволяет получить только индексы элементов списка,
# то enumerate() – сразу индекс элемента и его значение.
'''
spisok = [16, 46, 26, 36]
for i in enumerate(spisok):
    print(i)

(0, 16)
(1, 46)
(2, 26)
(3, 36)
'''

b = "hello"
for i in enumerate(b):
    print(i)
'''
(0, 'h')
(1, 'e')
(2, 'l')
(3, 'l')
(4, 'o')
'''