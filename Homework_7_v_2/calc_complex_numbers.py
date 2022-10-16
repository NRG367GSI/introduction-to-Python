def condition(meaning):
    if meaning == " ":
        return True
    else:
        return False



expression = "25+51i * (3+4i-5+6i)/(8+7i)"

        

def without_spaces(expression):
    
    new_expression = ""
    separation = expression.split()
    for i in separation:
        new_expression += i
    return new_expression

def complex_eval(expression):
    line = ""
    separation = []
    operation = "+-*/"

    
    if "(" in expression:
        index_start = expression.find("(")
        index_end = expression.find(")")
        brackets = expression[index_start + 1:index_end]
    print(expression[:index_start], expression[index_start + 1:index_end], expression[index_end + 1:], expression)
  



#print(complex_eval(without_spaces(expression)))

def complex_num1(seq):
    num_compl = []
    
    if "i" in seq:
        index_i = seq.find("i")
        index_plus = seq.find("+")
        num_compl.append(int(seq[:index_plus]))
        num_compl.append(int(seq[index_plus + 1:index_i]))
        seq = seq[index_i + 1:]
        print(num_compl, seq)
    
#complex_num(without_spaces(expression))

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
            str =""
            
    return arr

#pars(without_spaces(expression))

def complex_num(seq):
    oper = "+-*/()"
    operation = "+-"
    lin = []
    compl = []
    for i in range(len(seq)):
        
        if seq[i] in operation and "i" in seq[i+1]:
            compl.append(seq[i - 1])
            
            
            seq[i + 1] = seq[i + 1][:-1]
            compl.append(seq[i + 1])
            lin.append(compl)
            compl = []
            del seq[i-1:i+1]
    print(lin, seq)
'''          
            
        if seq[i] in oper:
            lin.append(seq[i])
'''
            


complex_num(pars(without_spaces(expression)))




        



