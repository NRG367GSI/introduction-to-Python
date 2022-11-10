#from write_data import *
import working_with_database as wwd
from birthday import get_birthday
import search_data as sd

def add_data():
    students = {}
    students['surname'] = input('Введите Фамилию: ').capitalize()
    students['name'] = input('Введите Имя: ').capitalize()
    if sd.search_name(students['surname'], students['name']) == None or len(students['surname']) == 0 and len(students['name']) == 0: # здесь надо проверять равно ли нулю
        students['hb'] = get_birthday() #input('Введите дату рождения(формат: дд.мм.гггг): ')
        students['class'] = input('Введите Класс: ')
        students['status'] = input('Введите успваймость по пятибальной системе: ') #успеваемость
        wwd.add_in_file(students)
        return 1 # надо хоть чтото возращать а то будет возращаться всегда None из else
    else:
        return None

    #print(students)


