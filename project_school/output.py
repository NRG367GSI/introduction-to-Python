def out(lin):
    for i in lin:
        
        print(f"{i['surname']}, {i['name']}, {i['hb']},    {i['class']},    {i['status']}")
    input("Нажмите Enter для продолжния работы: ")

#out(wwd.open_file())

import working_with_database as wwd
data = wwd.open_file()
for i in data:
    print(i.keys())