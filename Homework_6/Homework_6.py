from random import randint
#Задача 1. Создайте программу для игры в "Крестики-нолики".

def playing_field(rows = 3, columns = 3):
	field = [[0] * rows for _ in range(columns)]
	const = 1
	for i in range(rows):
		for j in range(columns):
			field[i][j] = const
			const += 1
	return field
	
def output_field(field):
	for i in field:
		print(i)
		
#output_field(playing_field())

def game(field):
	while (field[0][0] != field[0][1] != field[0][2] or
		   field[1][0] != field[1][1] != field[1][2] or
		   field[2][0] != field[2][1] != field[2][2] or
			  
		   field[0][0] != field[1][0] != field[2][0] or
		   field[0][1] != field[1][1] != field[2][1] or
		   field[0][2] != field[1][2] != field[2][2] or
			  
		   field[0][0] != field[1][1] != field[2][2] or
		   field[2][0] != field[1][1] != field[0][2]):
		#output_field(playing_field())
	
def draw():
	input("нажмите ВВОД, что бы бросить кубик!")
	user = int(randint(6))
	computer = int(randint(6))
	if user > computer:
		return True
	else:
		return False
		
draw()
	
			