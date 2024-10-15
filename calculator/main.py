from art import logo
from replit import clear

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

def calcuator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))    
  
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
  
    print(f' {num1} {operation_symbol} {num2} = {answer}')  
  
  # Ask the user if they want to continue with the calculation
    continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit")
    if continue_calculation == "n":
      should_continue = False
      clear()
      calcuator()
    else:
      num1 = answer
  
calcuator()  