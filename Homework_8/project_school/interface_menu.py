from read_data import *
from user_input import *
import search_data
import working_with_database as wwd
import search_data as sd
from output import out

def menu():
    menu = ['1', '2', '3', '4']
    point = None
    while point not in menu:
        print('''
Выбирите интерисующий пункт меню:\n 
1. Список всех учеников
2. Информация по конкретному ученику
3. Добавить ученика
4. Выход
''')
        point = input('Введите цифру: ')
        if point == '1':
            print('\nВесь список студентов:')
            out(wwd.open_file())
            
        elif point == '2':
            surname = input('Введите фамилию учиника: ')
            name = input('Введите имя учиника: ')
            
            #data = read_data()
            quesion = sd.search_name(surname, name)
            if quesion == None:
                print("Такой записи не существует!")
            else:
                print(quesion)
            # student = #search_data(request,data)
            # if student != None:
            #     print(student)
            # else:
            #     print('Такой ученик не найден!')
        elif point == '3':
            if add_data() == None:
                print("Такая запись существут!")
            else:
                print('Ученик успешно добавлен!')
        elif point == '4':
            print('До свидания')
            break
        else:
            print('\n--------------------------------------')
            print('Некорректный ввод, попробуйте еще раз!')
            print('--------------------------------------\n')
        point = None

