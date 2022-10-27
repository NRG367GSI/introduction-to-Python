import easygui as gui
import controller as cr

def submenu(): # Функция меню для удобного перехода к нужной задаче
    point = None
    msg = "Выбирите интерисующий пункт меню: "
    menu = ["Поиск по Фамилии Имени", "Поиск по дат рождения", "Список учащихся класса", "Успеваймость", "Назад в меню"]
    point = gui.choicebox(msg, choices = menu, title= "subMenu")
    if point == "Поиск по Фамилии Имени": gui.msgbox(cr.name_search())
    elif point == "Поиск по дат рождения": gui.msgbox(cr.birthdey_search())
    elif point == "Список учащихся класса": gui.msgbox(cr.grade_search())
    elif point == "Успеваймость": gui.msgbox(cr.performance_serch())
    elif point == "Назад в меню": return "beack"



def menu(): # Функция меню для удобного перехода к нужной задаче
	msg = "Выбирите интерисующий пункт меню: "
	menu = ["Список всех учеников", "Поиск с опцыямя", "Добавить запись", "Удалить Запись"]
	point = gui.choicebox(msg, choices = menu, title = "Menu")
	if point == "Список всех учеников": gui.msgbox(cr.list_file())
	if point == "Поиск с опцыямя": submenu()
	if point == "Добавить запись": cr.add_record()
	if point == "Удалить Запись": cr.deleted()
    
menu()


'''
4. Выход
'''