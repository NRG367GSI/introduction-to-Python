def get_expression():
    meaning = ""
    while meaning == "":
        meaning = input("Введите арифметические действия: ")
        if meaning == "":
            print("Вы ничего не ввели!")
        
    return meaning

def view_data(data, title):
    print(f'{title} = {data}')
