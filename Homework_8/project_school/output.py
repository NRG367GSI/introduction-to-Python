def out(lin):
    for i in lin:
        if len(i['surname']) < 15:
            i['surname'] = i['surname'] + " " * (14 - len(i['surname']))/2
        if len(i['name']) < 15:  
            i['name'] = i['name'] + " " * (15 - len(i['name']))
        print(f"{i['surname']}, {i['name']}, {i['hb']},    {i['class']},    {i['status']}")
    input("Нажмите Enter для продолжния работы: ")

#out(wwd.open_file())

import working_with_database as wwd
data = wwd.open_file()
for i in data:
    print(i.keys())