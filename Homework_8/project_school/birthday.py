import datetime
def get_day(): # Запрашивает консольный ввод пока не будет введено подходящее значени
    number = None
    while ValueError:
        try:
            while number == None or 0 >= number or 32 <= number:
                number = int(input("Введите число месяца рождения: "))
            return number
        except ValueError:
            print("Вы ввели не целое число, повторите ввод: ")

def get_month(): # Запрашивает консольный ввод пока не будет введено подходящее значени
    number = None
    while ValueError:
        try:
            while number == None or 0 >= number or 13 <= number:
                number = int(input("Введите месяц рождения: "))
            return number
        except ValueError:
            print("Вы ввели не целое число, повторите ввод: ")   

def get_year(): # Запрашивает консольный ввод пока не будет введено подходящее значени
    number = None
    while ValueError:
        try:
            while number == None or 1950 >= number or datetime.date.today().year <= number:
                number = int(input("Введите год рождения: "))
            return number
        except ValueError:
            print("Вы ввели не целое число, повторите ввод: ")        


def get_birthday():
    day = get_day()
    month = get_month()
    year =  get_year()
    return day, month, year


'''
d = datetime.date(year, month, day)

print(d.year) # 2012
print(d.day)  # 14
print(d.month) # 12
print(datetime.date.today())

##print(type(d))
'''
#Видимо не совместим с json
#print(get_birthday())

