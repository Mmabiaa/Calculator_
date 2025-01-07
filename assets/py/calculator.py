# calculator.py

import math

class Calculator:
    def evaluate(self, expression):
        try:
            return str(eval(expression))
        except Exception:
            return "Error"

    def advanced_operations(self, operation, value):
        try:
            if operation == 'sin':
                return str(math.sin(math.radians(float(value))))
            elif operation == 'cos':
                return str(math.cos(math.radians(float(value))))
            elif operation == 'tan':
                return str(math.tan(math.radians(float(value))))
            elif operation == '√':
                return str(math.sqrt(float(value)))
            elif operation == 'x²':
                return str(math.pow(float(value), 2))
            elif operation == '1/x':
                return str(1 / float(value))
            elif operation == 'log':
                return str(math.log10(float(value)))
            elif operation == 'pi':
                return str(math.pi)
            elif operation == '!':
                return str(math.factorial(int(value)))
            elif operation == '%':
                return str(float(value) / 100)
        except Exception:
            return "Error"