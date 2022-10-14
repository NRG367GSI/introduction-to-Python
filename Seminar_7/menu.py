import calc

def menu():
    menu = ["1", "0"]
    point = None
    while point not in menu:
        print('''
        1 - Калькулятор
        
        0 - Выход 
        ''')
        point = input("Введите, интерисующий пункт меню: ")

        if point == "1": print(calc.operatyon())

        if point == "0": break
        #point = None


menu()
