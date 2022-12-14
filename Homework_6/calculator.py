def calc(expression):
    try:  
        if '(' in expression:
            return calc(expression[expression.find('(')+1:expression.find(')')])
        if expression.find('+') >=0:
            return calc(expression[:expression.find('+')]) + calc(expression[expression.find('+')+1:])
        if expression.find('-') >=0:
            return calc(expression[:expression.find('-')]) - calc(expression[expression.find('-')+1:])
        if expression.find('*') >=0:
            return calc(expression[:expression.find('*')]) * calc(expression[expression.find('*')+1:])
        if expression.find('/') >=0:
            return calc(expression[:expression.find('/')]) / calc(expression[expression.find('/')+1:])
        return float(expression)
    except NameError:
        return "Неправильный запрос (400)"
    except ZeroDivisionError:
        return "Деление на ноль"
    except ValueError:
        return "ValueError"

print(calc(input("Введите выражение: ")))
