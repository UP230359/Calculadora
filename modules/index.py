import math
from custom_stack import Stack
from infix_to_postfix import infix_to_postfix

def evaluate_postfix(expression):
    stack = Stack()
    expression = infix_to_postfix(expression)
    tokens = expression.split()
    operators = {"+", "-", "*", "/", "^",
                 "log", "sin", "cos", "tan", 
                 "ln", "asin", "acos", "atan", 
                 "alog", "aln", "sqrt", "√"}

    for token in tokens:
        print(f"Processing token: {token}")
        
        if token not in operators:
            try:
                stack.push(float(token))
            except ValueError:
                print(f"Error converting token to number: {token}")
                return None
        else:
            if token in {"+", "-", "*", "/", "^"}:
                b, a = stack.pop(), stack.pop()
                try:
                    if token == "+":
                        result = a + b
                    elif token == "-":
                        result = a - b
                    elif token == "*":
                        result = a * b 
                    elif token == "/":
                        result = a / b
                    elif token == "^":
                        result = a ** b 
                    stack.push(result)       
                except Exception as e:
                    print(f"Error performing operation {token} = {result}: {e}")
                    return None
            else:
                x = stack.pop()
                print(f"Applying {token} to {x}")
                try:    
                    if token in ["asin", "acos"] and not (-1 <= x <= 1):
                        raise ValueError(f"{token} no acepta valores fuera de [-1, 1]")
                    elif token in ["sqrt", "√"] and x < 0:
                        raise ValueError(f"{token} no acepta valores negativos")
                    elif token == "sqrt" or token == "√":
                        result = math.sqrt(x)
                    elif token == "log":
                        result = math.log10(x)
                    elif token == "sin":
                        result = math.sin(math.radians(x))
                    elif token == "cos":
                        result = math.cos(math.radians(x))
                    elif token == "tan":
                        result = math.tan(math.radians(x))
                    elif token == "ln":
                        result = math.log(x)
                    elif token == "asin":
                        result = math.degrees(math.asin(x))
                    elif token == "acos":
                        result = math.degrees(math.acos(x))
                    elif token == "atan":
                        result = math.degrees(math.atan(x))
                    elif token == "alog":
                        result = math.pow(10, x)
                    elif token == "aln":
                        result = math.exp(x)
                    else:
                        raise ValueError(f"Función no reconocida: {token}")
                    stack.push(result)
                except ValueError as ve:
                    print(f"Math error in {token}({x}): {ve}")
                    return None
                except Exception as e:
                    print(f"Error processing function {token}: {e}")
                    return None
    
    return stack.pop()