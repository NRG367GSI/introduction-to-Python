def user_input():
    meaning = ""
    while meaning == "":
        meaning = input("Введите арифметические действия: ")
        if meaning == "":
            print("Вы ничего не ввели!")
        
    return meaning

