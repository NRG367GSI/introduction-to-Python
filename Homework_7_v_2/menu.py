import controller as cr
import loger as lg

def menu():
    menu = ["1", "2", "0"]
    point = None
    print("\n       Калькулятор запущен\n")
    while point not in menu:
        print("Меню:\n"
              "1 - Калькулятор с рациональными числами\n"
              "2 - Калькулятор с комплексными числами\n"
              "3 - Просмотр истории\n"
              "0 - Выход\n"
              )
        point = input("Введите, интерисующий пункт меню: ")

        if point == "1":
            print("\n-----------------------------------------------")
            print("Выбран режим для работы с рациональными числами")
            print("-----------------------------------------------\n")
            cr.control_calc()
            

        elif point == "2":
            print("\n----------------------------------------------")
            print("Выбран режим для работы с комплексными числами")
            print("----------------------------------------------\n")
            cr.control_complex_calc()

        elif point == "3":
            lg.read()

        elif point == "0":
            break

        else:
            print("\n--------------------------------------")
            print("Некорректный ввод, попробуйте еще раз!")
            print("--------------------------------------\n")
        point = None

menu()
