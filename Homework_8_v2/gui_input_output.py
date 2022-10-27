import easygui as gui
import datetime
def output(lin):
    sum = ""
    result = ""
    for i in lin:
        for j in i:
            if len(i[j]) < 12:
                sum += str(" " * int((12 - len(i[j]))/2)) + str(i[j]) + str(" " * int((12 - len(i[j]))/2))
        result += sum + "\n"
        sum = ""
    return result

def input_name():
    data = ["", ""]
    msg = "Введите фамилию и имя:"
    title  =  "Ввод данных"
    field_names  =  ["Фамилия: ", "Имя: "]
    try:
        while len(data[0]) == 0 or len(data[1]) == 0:
            data = gui.multenterbox(msg, title, field_names)
        return data[0].capitalize(), data[1].capitalize()
    except TypeError:
        return None

def input_birthday():
    day = [i for i in range(1, 32)]
    month = [i for i in range(1, 13)]
    year = [i for i in range(1950, datetime.date.today().year+1)]
    data = ["0", "0", "0"]
    msg = "Введите Дату рождения:"
    title  =  "Ввод данных"
    field_names  =  ["Чсло: ", "Месяц: ", "Год"]
    try:
        while int(data[0]) not in day or int(data[1]) not in month or int(data[2]) not in year:

            data= [int(i) for i in gui.multenterbox(msg, title, field_names)]
        return data
    except ValueError:
        return input_birthday()

def clas():
    num = [str(i) for i in range(1,11)]
    letter = "укнгзвапроджмитбю"
    clas = []
    grade =""
    for j in range(len(num)):
        for k in range(len(letter)):
            grade = num[j] + letter[k]
            clas.append(grade)
            clas.sort()
            grade =""
    return clas

def input_clas():
    grade = clas()
    data = [""]
    msg = f"Введите класс учащегося из списка: \n {grade}"
    title  =  "Ввод данных"
    field_names  =  ["класс"]
    try:
        while len(data[0]) == 0 or data[0] not in grade:
            data = gui.multenterbox(msg, title, field_names)
        return data
    except TypeError:
        return None

def input_performance():
    performance = ["1", "2", "3", "4", "5"]
    msg = f"Введите успеваймость учащегося из списка: \n {performance}"
    title  =  "Ввод данных"
    field_names  =  ["1", "2", "3", "4", "5"]
    data = 0
    try:
        while data not in performance:
            data = gui.buttonbox(msg, title, field_names)
        return str(data)
    except TypeError:
        return None

def none_output():
    return  gui.msgbox(msg ="Записей нет!",  title ="Окно информации")

def addad():
    return  gui.msgbox(msg ="Запись успешно добавлена!",  title ="Окно информации")

def exist():
    return  gui.msgbox(msg ="Запись существует!",  title ="Окно информации")

def del_print():
    return  gui.msgbox(msg ="Удалние прошло успешно!",  title ="Окно информации")







    
    