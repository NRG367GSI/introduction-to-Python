import json
import easygui as gui
from random import randrange
def save(BD):
	with open('BD.json', 'a', encoding = 'utf-8') as saves:
		saves.write(json.dumps(BD, ensure_ascii=False))
		print("База данных сохранена!")

# задача 1. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
def multipliers_number(number):
	#number = get_int()	
	list_multipliers = []
	for i in range(1, number):
		multipliers = []
		if number%i == 0:
			multipliers.append(i)
			multipliers.append(int(number/i))
			list_multipliers.append(multipliers)
	return list_multipliers

def multipliers_number_gui():
	number = gui.integerbox("Введите число от 0 до 1000, множители которого нужно получить:", lowerbound=-1000, upperbound=1000)
	result = multipliers_number(number)
	gui.msgbox(result, "Результат: ")
	save(result)


#задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def get_sequence(min, max, size):
		seq = []
		for _ in range(size):
			seq.append(randrange(min, max))
		return seq

def unique_number(seq):
		print(seq)
		unique = []
		for i in seq:
			if i not in unique:
				unique.append(i)
		return "Изночальная последовательность: ", seq, "\n", "Результат: ", unique
		
def unique_number_gui():
	min = 0
	max = 0
	while not min < max:
		min = gui.integerbox("Введите min от -1000 до 1000:", lowerbound=-1000, upperbound=1000)
		max = gui.integerbox("Введите max от -1000 до 1000:", lowerbound=-1000, upperbound=1000)
		if not min < max:
			gui.msgbox("min не меньше max, повторите ввод:", "Ошибка: ", ok_button="[y]es")

	size = gui.integerbox("Введите size от 0 до 1000:", lowerbound=0, upperbound=100)
	result = unique_number(get_sequence(min, max, size))
	gui.msgbox(result, "Результат: ", ok_button="[y]es")
	save(result)
	
# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
#*Пример:* 
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def degre_polinomial(k):
	result = ""
	plus = "+"
	x = "x"
	star = "**"
	for i in range(k + 1, 0, -1):
		ratio = str(randrange(0, 100))
		if i > 2 and ratio != "0":
			result += ratio + "*" + x + star + str(i - 1) + plus
		elif i < 2:
			result += ratio + "*" + x + plus + ratio + " = 0"
		elif ratio == 0: continue
	return result

def interfeice_degre_polinomial():
	fin = int(gui.enterbox(msg="Задайте натуральную степень:",title = "Многочлен степени"))
	result = degre_polinomial(fin)
	gui.msgbox(result, "Результат: ")
	save(result)


#Задача 4. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

def least_multiple(a, b):
	if a < b:
		for number in range(2, a):
			if a%number == 0 and b%number == 0:
				return number
		else:
			return "значение не найдено"
	elif b < a:
		for number in range(2, b):
			if a%number == 0 and b%number == 0:
				return number
		else:
			return "значение не найдено"

def least_multiple_gui():
	a = gui.integerbox("Введите первое число от -1000 до 1000:", lowerbound=-1000, upperbound=1000)
	b = gui.integerbox("Введите второе число от -1000 до 1000:", lowerbound=-1000, upperbound=1000)
	result = least_multiple(a, b)
	gui.msgbox(f"Наименьшее общее кратное: {result} двух чисел {a} и {b}", "Результат: ", ok_button="[y]es")
	save(result)

def menu(): # Функция меню для удобного перехода к нужной задаче
	msg = '''
        1 - задача 1. Cоставит список простых множителей числа N.
        2 - задача 2. Выведет список неповторяющихся элементов исходной последовательности.
        3 - задача 3. Сформировать случайным образом список коэффициентов многочлена.
        4 - задача 4. Находит наименьшее общее кратное двух чисел.
        '''
	menu = ["1", "2", "3", "4"]
	point = gui.buttonbox(msg, choices = menu, title = "Menu")
	if point == "1": multipliers_number_gui()
	if point == "2": unique_number_gui()
	if point == "3": interfeice_degre_polinomial()
	if point == "4": least_multiple_gui()
menu()


