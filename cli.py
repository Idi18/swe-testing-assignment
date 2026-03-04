from calculator import Calculator

calc = Calculator()

def calculate(a, operator, b):
    if operator == "+":
        return calc.add(a, b)
    if operator == "-":
        return calc.subtract(a, b)
    if operator == "*":
        return calc.multiply(a, b)
    if operator == "/":
        return calc.divide(a, b)
    raise ValueError("Invalid operator")