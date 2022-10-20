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
#print(calc(stroka))

def condition(meaning):
    if meaning == " ":
        return True
    else:
        return False
        


def without_spaces(expression):
    
    new_expression = ""
    separation = expression.split()
    for i in separation:
        new_expression += i
    return new_expression
    
def pars(seq):
    operation = "+-*/()"
    str = ""
    arr = []
    for i in range(len(seq)):
        str += seq[i]
        if seq[i] in operation:
            str = str[:-1]
            arr.append(str)
            arr.append(seq[i])
            str = ""
            while "" in arr:
            	arr.remove("")
    return arr
    '''
def del_s(arr):
    
    return arr    
    '''
def complex_num(seq):
    oper = "+-*/()"
    operation = "+-"
    lin = []
    compl = []
    #print(seq)
    for i in range(len(seq) - 1):
    	if seq[i] in oper:
    		#print(seq[i])
    		#compl.append(seq[i])
    		
    		lin.append(seq[i])
    		#compl = []
    		#print(lin)
    		
    	if seq[i] in operation and "i" in seq[i+1]:
            compl.append(seq[i - 1])
            
            
            seq[i + 1] = seq[i + 1][:-1]
            compl.append(seq[i + 1])
            lin.append(compl)
            compl = []
            
            
    print(lin)
'''          
            
        if seq[i] in oper:
            lin.append(seq[i])
'''
            

expression = "(25+51i * (3+4i-5+6i))/(8+7i)"
#print(pars(without_spaces(expression)))
complex_num(pars(without_spaces(expression)))
