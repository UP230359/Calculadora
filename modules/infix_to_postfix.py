from custom_stack import Stack
from custom_queue import Queue
import math
import re

def add_spaces(expression):
    # Asegura que las funciones como sqrt( se tokenicen correctamente
    return " ".join(re.findall(r'\d+\.\d+|\d+|[+\-*/^()]|\w+|√', expression))

def infix_to_postfix(expression):
    expression = add_spaces(expression)
    precedence = { 
        "+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": 0,
        "log": 4, "ln": 4, "sin": 4, "cos": 4, "tan": 4,
        "alog": 4, "aln": 4, "asin": 4, "acos": 4, "atan": 4,
        "sqrt": 4, "√": 4
    }
    function_names = {"sqrt", "log", "ln", "sin", "cos", "tan", "alog", "aln", "asin", "acos", "atan", "√"}
    
    stack = Stack()
    queue = Queue()
    tokens = expression.split()  # Sin paréntesis adicionales
    
    for token in tokens:
        if token == "(":
            stack.push(token)
        elif token == ")":
            while not stack.is_empty() and stack.peek() != "(":
                queue.enqueue(stack.pop())
            stack.pop()  # Eliminar el "("
            # Si el tope es una función, agregarla a la cola
            if not stack.is_empty() and stack.peek() in function_names:
                queue.enqueue(stack.pop())
        elif token in function_names:
            stack.push(token)
        elif token in precedence:
            while (not stack.is_empty() and stack.peek() != "(" 
                   and precedence[token] <= precedence.get(stack.peek(), 0)):
                queue.enqueue(stack.pop())
            stack.push(token)
        elif token.lower() in ("π", "pi"):
            queue.enqueue(math.pi)
        elif token.lower() == "e":
            queue.enqueue(math.e)
        else:
            try:
                queue.enqueue(float(token))
            except ValueError:
                raise ValueError(f"Token inválido: {token}")
    
    # Vaciar la pila al final
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    
    return " ".join(str(queue.dequeue()) for _ in range(queue.size))

