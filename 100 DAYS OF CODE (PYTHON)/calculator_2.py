from calculator_art import logo
import os

#  creating functions for each operation
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2



# storing each key to the adequate function above.
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  #  printing each of the keys(symbols) from the dictionary: operations, to make the user choose which operation he/she wants to use.
  for symbol in operations:
    print(symbol)
  
  restart = True
#  the while loop keeps the program running until the user wants it to stop.
  while restart:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")

#    asking if the user wants to continue making any other calculations, if yes, it keeps calculating with the previous answer, else, it starts a new calculation with  different numbers and operations.

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      restart = False
      os.system('cls')
      calculator()



calculator()


