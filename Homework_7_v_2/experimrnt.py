stroka=input('Введите числа: ')
def calc(expression):
    if '(' in expression:
        return calc(expression[expression.find('(')+1:expression.find(')')])
    if expression.find('+') >=0: #if '+' in stroka
        return calc(expression[:expression.find('+')]) + calc(expression[expression.find('+')+1:])
    if expression.find('-') >=0: #if '+' in stroka
        return calc(expression[:expression.find('-')]) - calc(expression[expression.find('-')+1:])
    if expression.find('*') >=0: #if '+' in stroka
        return calc(expression[:expression.find('*')]) * calc(expression[expression.find('*')+1:])
    if expression.find('/') >=0: #if '+' in stroka
        return calc(expression[:expression.find('/')]) / calc(expression[expression.find('/')+1:])
    return int(expression)
print(calc(stroka))

