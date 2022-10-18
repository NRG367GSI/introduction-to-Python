import user_interface as ui
def calc_compiex(expression):
    try: 
        return eval(expression)
    except NameError:
        return "Неправильный запрос (400)"
    except ZeroDivisionError:
        return "Деление на ноль"
    except ValueError:
        return "ValueError"

print(calc_compiex(input("введите выражение")))#ui.user_input()))
