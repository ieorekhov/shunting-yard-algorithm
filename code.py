tokens = input()
length = len(tokens) - 1

def isdigit(token):
    try:
        token = int(token)
        return True
    except  ValueError:
        return False

def last(operands):
    return operands[-1] if operands else None

def more_worthy(last, token):
    d = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}
    return d[last] >= d[token]

def evaluate(tokens):
    operators = []
    operands = []
    for i in range(0, length, 2):
        token = tokens[i]
        if(token.isdigit()):
            operands.append(token)
        elif(token=="("):
            operators.append(token)
        elif(token==")"):
            lastt = last(operators)
            while(lastt != "(")and(lastt != None):
                end = operators.pop()
                operands.append(end)
            operators.pop()    
        else:
            top = last(operators)
            while(top != None)and(more_worthy(top, token)):
                end = operators.pop()
                operands.append(end)
            operators.append(token)
            
evaluate(tokens)
print(operators)
