# задача 1. Создайте программу для игры с конфетами человек против человека. На столе лежит 2021 конфета. 
# За 1 ход можно забрать не более 28 конфет
import random
import json
candy = ["candy"] * 2021
user_took = []
computer_took = []

def user_step(candy, user_took):
	print("Возьмите конфеты от 1 до 28: ")
	motion = int(input("Сколько конфет возьмете?"))
	for i in range(motion):
		user_took.append(candy[i])
		candy.pop(i)
	return len(candy), user_took
		
def computer_step(candy, computer_took):
	if len(candy) > 56:
		motion = 28
	elif len(candy) < 56:
		motion = len(candy) - 28
	elif len(candy) < 28:
		motion = len(candy)
		
	for i in range(motion):
		computer_took.append(candy[i])
		candy.pop(i)
	return len(candy), computer_took
		
def toss():
	input("жеребьевка: ")
	toss_user = random.randint(1, 6)
	toss_computer = random.randint(1,6)
	if toss_user < toss_computer:
		return True
	else:
		return False

def game(candy, user_took, computer_took):
	if False:
		while len(candy) != 0:
			print(len(candy), len(user_took), len(computer_took))
			user_step(candy, user_took)
			computer_step(candy, computer_took)
	else:
		while len(candy) != 0:
			print(len(candy), len(user_took), len(computer_took))
			computer_step(candy, computer_took)
			user_step(candy, user_took)

#game(candy, user_took, computer_took)

# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def packing(line):
	arr = []
	count = 1
	result = []
	for i in range(len(line)):
		if len(arr) == 0:
			arr.append(line[i])
		elif arr[-1] == line[i]:
			count += 1
		elif arr[-1] != line[i]:
			arr.append(count)
			result.append(arr)
			arr = []
			count = 1
			arr.append(line[i])
		if i == len(line) - 1:
			arr.append(count)
			result.append(arr)
	return result
	
#print(packing(line))

def unpacking(arr):
	text = ""
	for i in arr:
		text += i[0] * i[1]
	return text

def open_file():
	with open("BD.json", "r", encoding="utf-8") as file:
		data = json.load(file)
		return data

def save(BD):
	with open('BD.json', 'w', encoding = 'utf-8') as saves:
		saves.write(json.dumps(BD, ensure_ascii=False))
		print("База данных сохранена!")



#save(packing(open_file()))

print(unpacking(open_file()))
	
		



			




	
	
	




	

	


