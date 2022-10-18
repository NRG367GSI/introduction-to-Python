def operatyon(data):
    return eval(data)


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


def complex_num(seq):
    for i in range(len(seq)):
        if seq[i] == "+":
            print(i)

            

expression = "(2 + 2j * (4j - 5))/(4+4j)"

#print(pars(without_spaces(expression)))

print(operatyon(input("compl =")))


