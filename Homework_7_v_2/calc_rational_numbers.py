import user_interface as ui
def operatyon(data):
    try:
        return eval(data)
    except NameError:
        return "Неправильный запрос (400)"
    except ZeroDivisionError:
        return "Деление на ноль"

print(operatyon(ui.user_input()))
