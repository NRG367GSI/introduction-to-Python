from random import randint
#Задача 1. Создайте программу для игры в "Крестики-нолики".

def playing_field(rows = 3, columns = 3):
	field = [[0] * rows for _ in range(columns)]
	const = 1
	for i in range(rows):
		for j in range(columns):
			field[i][j] = str(const)
			const += 1
	return field
	
def output_field(field):
	for i in field:
		print(i)

def game_ower(field):
	if field[0][0] == field[0][1] == field[0][2] or\
		field[1][0] == field[1][1] == field[1][2] or\
		field[2][0] == field[2][1] == field[2][2] or\
		field[0][0] == field[1][0] == field[2][0] or\
		field[0][1] == field[1][1] == field[2][1] or\
		field[0][2] == field[1][2] == field[2][2] or\
		field[0][0] == field[1][1] == field[2][2] or\
		field[2][0] == field[1][1] == field[0][2]:
		return True
	else:
		return False

def draw(arr):
	seq = len(arr) * len(arr[0])
	x = 0
	o = 0
	for i in arr:
		for j in i:
			if j == "X":
				x += 1
			if j == "O":
				o += 1
	if seq - x - o == 0:
		return True
	else:
		return False

def first_player(arr):
	x = ""
	user = "X"
	while x == "":
		x = input("Ваш ход: ")
		if x in arr[0] or x in arr[1] or x in arr[2]:
			for i in range(len(arr)):
				for j in range(len(arr[i])):
					
					if arr[i][j] == x:
						arr[i][j] = user
		else:
			x = ""

def second_player(arr):
	x = ""
	user = "O"
	while x == "":
		x = input("Ваш ход: ")
		if x in arr[0] or x in arr[1] or x in arr[2]:
			for i in range(len(arr)):
				for j in range(len(arr[i])):
					if arr[i][j] == x:
						arr[i][j] = user
		else:
			x = ""
				
def lottery():
	input("Кидает кубик игрок, 1 нажмите Enter")
	player_1 = randint(1,6)
	print(f"Игрок 1 выкинул: {player_1}")
	input("Кидает кубик игрок 2,  нажмите Enter")
	player_2 = randint(1,6)
	print(f"Игрок 2 выкинул: {player_2}")
	input("Нажмите Enter для продолжения: ")
	if player_1 > player_2:
		return "X"
	else:
		return "O"

def step_x(maps):
	print("Ход игрока 1: ")
	output_field(maps)
	first_player(maps)
	return maps

def step_o(maps):
	print("Ход игрока 2: ")
	output_field(maps)
	second_player(maps)
	return maps

def game():
	lot = lottery()
	cond = False
	maps = playing_field()
	if lot == "X":
		while cond != True:
			print("Ход игрока 1: ")
			output_field(maps)
			first_player(maps)
			

			cond = game_ower(maps)
			if cond == True:
				print("Игра окончена, победил игрок 1")
				output_field(maps)
				break
			dr = draw(maps)
			if dr == True:
				output_field(maps)
				print("Ничья!")
				break
			print("Ход игрока 2: ")
			output_field(maps)
			second_player(maps)
			cond = game_ower(maps)
			if cond == True:
				print("Игра окончена, победил игрок 2")
				output_field(maps)
				break
	
			dr = draw(maps)
			if dr == True:
				output_field(maps)
				print("Ничья!")
				input("Нажмите Enter для выхода!")
				break
	else:
		while cond != True:
			print("Ход игрока 2: ")
			output_field(maps)
			second_player(maps)
			cond = game_ower(maps)
			if cond == True:
				print("Игра окончена, победил игрок 2")
				output_field(maps)
				break
			dr = draw(maps)
			if dr == True:
				output_field(maps)
				print("Ничья!")
				break
			print("Ход игрока 1: ")
			output_field(maps)
			first_player(maps)
			cond = game_ower(maps)
			if cond == True:
				print("Игра окончена, победил игрок 1")
				output_field(maps)
				break
	
			dr = draw(maps)
			if dr == True:
				output_field(maps)
				print("Ничья!")
				input("Нажмите Enter для выхода!")
				break

game()


