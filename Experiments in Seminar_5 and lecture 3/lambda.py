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

b = "hello"
for i in enumerate(b):
    print(i)

(0, 'h')
(1, 'e')
(2, 'l')
(3, 'l')
(4, 'o')

Эти кортежи можно распаковывать, то есть извлекать индекс и значение, в теле цикла:

>>> for item in enumerate(spisok):
...     print(item[0], item[1])
... 
0 16
1 46
2 26
3 36
Однако чаще это делают еще в заголовке for, используя две переменные перед in:

>>> for id, val in enumerate(spisok):
...     print(id, val)
... 
0 16
1 46
2 26
3 36
Функция enumerate() используется для упрощения прохода по коллекциям в цикле,
0когда кроме самих элементов требуется их индекс:

>>> a = [10, 20, 30, 40]
>>> for id, item in enumerate(a):
...     a[id] = item + 5
... 
>>> a
[15, 25, 35, 45]

'''

# Работа с файлами
#Открытие файла f = open('text.txt', 'r')

#Чтение из файла, в скобках можно указать сколько символов считывать
'''
f = open('text.txt')
f.read(1) #'H'
f.read() #'ello world!\nThe end.\n\n'
'''

# Чтение файла построчно
'''
f = open('text.txt')
for line in f:
    print(line)
'''

#Запись в файл
'''
l = [str(i)+str(i-1) for i in range(20)] #['0-1', '10', '21', '32']
f = open('text.txt', 'w')
for index in l:
    f.write(index + '\n')
f.close()
'''

# string.strip(string[, chars]) -> str
#Возвращает копию указанной строки, с обоих концов которой устранены указанные символы.
'''
import string
string.strip('abca', 'ac')  # 'b'
'''

# Метод файла file.writelines() записывает последовательность (список) строк в файл file,
# не добавляет разделители строк автоматически
# Записать сразу все строки, разделенные разделителем строк \n, можно используя метод файла file.write().
'''
text = [
        'This is 1st line\n', 
        'This is 2nd line\n', 
        'This is 3rd line\n'
        ]
fp = open('foo.txt', 'w')
fp.writelines(text)
fp.close()

# Запишет
# This is 1st line
# This is 2nd line
# This is 3rd line
'''

# Функцию open() предпочтительнее использовать с оператором контекстного менеджера with.
# При использовании оператора with файл закрывать не нужно:
'''
text = [
        'This is 1st line\n', 
        'This is 2nd line\n', 
        'This is 3rd line\n']

# пишем
with open('foo.txt', 'w') as fp:
    fp.writelines(text)

# читаем, что получилось
with open('foo.txt', 'r') as fp:
    print(fp.read())

# This is 1st line
# This is 2nd line
# This is 3rd line

'''
# Кортежи
# Меньше размер
'''
a = (1, 2, 3, 4, 5, 6)
b = [1, 2, 3, 4, 5, 6]
a.__sizeof__() #36
b.__sizeof__() #44

Возможность использовать кортежи в качестве ключей словаря:
>>>
>>> d = {(1, 1, 1) : 1}
>>> d
{(1, 1, 1): 1}
>>> d = {[1, 1, 1] : 1}

Создаем пустой кортеж:

>>>
>>> a = tuple() # С помощью встроенной функции tuple()
>>> a
()
>>> a = () # С помощью литерала кортежа
>>> a
()
>>>
>>> a = tuple('hello, world!')
>>> a
('h', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!')

поменять местами значения двух переменных:

a, b = b, a
'''






#Содержание раздела:
'''
ОБЗОРНАЯ СТРАНИЦА РАЗДЕЛА
Метод file.close(), закрывает файл.
Метод file.flush(), очищает буфер чтения.
Метод file.fileno(), получает файловый дескриптор.
Метод file.isatty(), проверяет связь с терминалом.
Метод file.read(), читает весь файл или кусками.
Метод file.readline(), читает файл построчно.
Метод file.readlines(), получает список строк файла.
Метод file.seek(), перемещает указатель в файле.
Метод file.tell(), позиция указателя в файле.
Метод file.truncate(), усекает размер файла.
Метод file.write(), пишет данные в файл.
Метод file.writelines(), пишет список строк в файл.

РЕКЛАМА

practicum.yandex.ru
Изучение программирования на Java
Курсы от Яндекса!
Вводная часть курса — бесплатно. 78% выпускников трудоустраиваются. Начни сейчас.
Узнать больше
https://docs-python.ru/tutorial/metody-fajlovogo-obekta-potoka-python/metod-file-writelines/
'''



