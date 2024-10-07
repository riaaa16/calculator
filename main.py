'''importing calculations'''
# `Dict` and `Type` are used here for type hinting to indicate that the dictionary `operations_map`
# will have keys of type `str` and values that are calculation class types.
from typing import Dict, Type
from app.calculation import Addition, Subtraction, Multiplication, Division
from app.calculator import Calculator
from app.history import HistoryManager

# Mapping operation strings to respective calculation classes
# dictionary[key,value]
# key is the string representing the operation
# value is the corresponding class that performs the operation
operations_map: Dict[str, Type] = {
    'add': Addition,
    'subtract': Subtraction,
    'multiply': Multiplication,
    'divide': Division
}

class CommandProcessor:
    '''
    processes user commands, performs calculations, interacts with Calculator and HistoryManager
    '''
    def __init__(self) -> None:
        '''initializes CommandProcessor with a Calculator instance.'''
        self.calculator = Calculator()

    def execute(self, command: str) -> None:
        '''
        executes given command, processes operation, returns result
        '''
        # splits user input into 3 parts (operation, a, b)
        parts = command.split()

        # if there isn't 3 parts, print error
        # example of LBYL
        if len(parts) != 3:
            print("Invalid command format. Type 'help' for instructions.")
            return

        # separates parts into operation and two arguments
        operation, a_str, b_str = parts

        try:
            # try to convert input into floats
            # if this fails, value error is raised
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("Invalid numbers. Please enter valid numeric values.")
            return
        
        # LBYL -> if operation not in operations_map, print error
        if operation not in operations_map:
            print(f"Unknown operation '{operation}'. Type 'help' for instructions.")
            return

        # instantiates appropriate calculation class based on the 3 parts passed in
        # dynamic -> strategy design pattern
        # lets us get rid of if statements checking for which operation
        calculation_class = operations_map[operation]
        calculation = calculation_class.create(a,b)

        # perform calculation and print result
        try:
            result = self.calculator.perform_operation(calculation)
            print(f"Result: {result}")
            print(f"Operation: {calculation}") # uses __str__ of Calculation class
        except ZeroDivisionError:
            print("Error: Division by zero.")

    def show_help(self) -> None:
        '''displays help menu and available commands'''
        print('''
Available commands:
  add a b        - Adds a and b
  subtract a b   - Subtracts b from a
  multiply a b   - Multiplies a and b
  divide a b     - Divides a by b
  history        - Shows the operation history
  undo           - Undoes the last operation
  clear          - Clears the operation history
  exit           - Exits the REPL
  help           - Shows this help message
''')

    def show_history(self) -> None:
        '''displays full history of operations performed'''
        history = self.calculator.get_history()
        if not history:
            print("The history is empty!")
        else:
            # lists number and what operation was performed
            for index, command in enumerate(history, start=1):
                print(f"{index}: {command.operation}")

    def undo_last(self) -> None:
        '''undoes and displays the last operation'''
        last_operation = self.calculator.undo()
        if last_operation:
            print(f"Undid operation: {last_operation.operation}")
        else:
            print("No operation to undo.")

    def clear_history(self) -> None:
        '''clears operation history'''
        self.calculator.clear_history()
        print("History cleared.")

def main():
    '''REPL is implemented here'''
    # creating instance of CommandProcessor
    processor = CommandProcessor()
    print("Welcome to the Calculator REPL. Type 'help' for instructions or 'exit' to quit.")

    while True:
        # strips white space and converts to lowercase
        command = input(">>> ").strip().lower()
        # checks input for 'exit' or 'quit'
        if command in ['exit', 'quit']:
            print("Goodbye!")
            # if 'exit' or 'quit' exit loop and program
            break
        elif command == 'help':
            processor.show_help()
        elif command == 'history':
            processor.show_history()
        elif command == 'undo':
            processor.undo_last()
        elif command == 'clear':
            processor.clear_history()
        else:
            # if asking for help or history functions, compute command
            processor.execute(command)

# checks if this script is being run as the main program and not as a module
if __name__ == '__main__':
    main()
