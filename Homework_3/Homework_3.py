# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
import random
def random_sequence(min, max, size): # Генерирует список из случайных целых значений
    seq = []
    while len(seq) < size:
        i = randrange(min, max)
        seq.append(i)
    return seq

def sum_odd_elements(seq):
    sum = 0
    for i in range(len(seq)):
        if i%2 != 0:
            sum += seq[i]
    return seq, sum

#print(sum_odd_elements(random_sequence(0,10,10)))

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def multiplication_pairs_number(seq): #перемножает пары значений массива
    start_position = 0
    end_position = -1
    seq2 = seq
    mult = []
    while len(seq) != 0:
        if len(seq) > 1:
            mult.append(seq[start_position] * seq[end_position])
            seq.pop(start_position)
            seq.pop(end_position)
        elif len(seq) == 1:
            break
    return mult

#print(multiplication_pairs_number(random_sequence(0,10,11)))

# Задача 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def real_numbers_seq(size): # генерирует массив случайных вещественных чисел
    seq = [0] * size
    for i in range(size):
        seq[i] = round(random.random(), 5)
    return seq

def fractional_part(seq): # приводит к целому виду значения массива
    seq_fract = []
    for number in seq:
        if number < 0:
            number = -1 * number
        while number % 1 != 0:
            number = round(number, 5) * 10
        seq_fract.append(int(number))
    return seq_fract

def difference_max_min(seq): # находит разность максимального и минемального элемента массива
    min = seq[0]
    max = seq[0]
    for i in seq:
        if i < min:
            min = i
        elif i > max:
            max = i 
    return max, min, max - min

#print(difference_max_min(fractional_part(real_numbers_seq(10))))

# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное
def dec_bin(number): # десятичное предстовление числа, представляет в бинарном виде, аналог bin(number)
    future_bin = ""
    bin = ""
    while number > 0:
        future_bin += str(number % 2)
        number = int(number / 2)
    while len(future_bin) != 0:
        bin += future_bin[-1]
        future_bin = future_bin[0:len(future_bin) - 1]
    return "0b" + bin

# Задача 5 
def get_int(): # Запрашивает консольный ввод пока не будет введено целое число
    number = None
    while ValueError:
        try:
            number = int(input("Введите целое число: "))
            return number
        except ValueError:
            print("Вы ввели не целое число, повторите ввод: ")

def get_sequence(): # Создает матрицу, заполненную случайными значениями
    rows = 1
    columns = 1
    while rows % 2 != 0 or columns % 2 != 0:
        print("Введите число строк матреци: ")
        rows = get_int()
        print("Введите число колонок матреци: ")
        columns = get_int()
    print("Введите минемальное значение элемента матреци: ")
    min = get_int()
    print("Введите максимальное значение элемента матреци: ")
    max = get_int()
    seq =[[0] * rows for _ in range(columns)]
    for i in range(len(seq)):
        for j in range(len(seq[i])):
            seq[i][j] = random.randint(min, max)  
    return seq

def output_matrix(seq):
    for i in seq:
        print(i)

def mix_matrix(seq):
    output_matrix(seq)
    
    rows_index = [i for i in range(len(seq[0]))]
    columns_index = [j for j in range(len(seq))]
    for i in range(int((len(seq) * len(seq[0]))/2)):
        print(i, rows_index, columns_index)
        

        rows_1 = random.choice(rows_index)
        rows_index.pop(rows_index.index(rows_1))

        columns_1 = random.choice(columns_index)
        columns_index.pop(columns_index.index(columns_1))

        rows_2 = random.choice(rows_index)
        rows_index.pop(rows_index.index(rows_2))   

        columns_2 = random.choice(columns_index)
        columns_index.pop(columns_index.index(columns_2))
        temp = seq[rows_1][columns_1]
        seq[rows_1][columns_1] = seq[rows_2][columns_2]
        seq[rows_2][columns_2] = temp
    output_matrix(seq)
        
    
    
mix_matrix(get_sequence())

 

