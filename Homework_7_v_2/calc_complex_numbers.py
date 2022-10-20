def complex_calc(expression):
    try: 
        return eval(expression)
    except NameError:
        return "Неправильный запрос (400)"
    except ZeroDivisionError:
        return "Деление на ноль"
    except ValueError:
        return "ValueError"

