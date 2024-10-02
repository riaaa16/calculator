'''importing calculations'''
# Importing necessary typing utilities.
# `Dict` and `Type` are used here for type hinting to indicate that the dictionary `operations_map`
# will have keys of type `str` and values that are calculation class types.
from typing import Dict, Type

from app.calculation import Addition, Subtraction, Multiplication, Division

# Mapping operation strings to respect calculation classes
# dictionary[key,value]
# key is the string representing the operation
# value is the corresponding class that performs the operation
operations_map: Dict[str, Type] = {
    'add': Addition,
    'subtract': Subtraction,
    'multiply': Multiplication,
    'divide': Division
}

def main():
    '''REPL is implemented here'''
    print("Welcome to the Calculator REPL. Type 'help' for instructions or 'exit' to quit.")

    while True:
        # strips white space
        command = input(">>> ").strip()
        # checks lowercase input for 'exit' or 'quit'
        if command.lower() in ['exit', 'quit']:
            print("Goodbye!")
            # if 'exit' or 'quit' exit loop and program
            break
        elif command.lower() == 'help':
            print("""
Available commands:
  add a b        - Adds a and b
  subtract a b   - Subtracts b from a
  multiply a b   - Multiplies a and b
  divide a b     - Divides a by b
  exit           - Exits the REPL
  help           - Shows this help message
""")
        # all other inputs get processed as calculations
        else:
            # splits user input into 3 parts (operation, a, b)
            parts = command.split()
            # if there isn't 3 parts, print error
            # example of LBYL
            if len(parts) != 3:
                print("Invalid command format. Type 'help' for instructions.")
                continue # skips rest of loop and prompts for the next command

            # separates parts into operation and two arguments
            operation, a_str, b_str = parts
            try:
                # try to convert input into floats
                # if this fails, value error is raised
                a = float(a_str)
                b = float(b_str)

                # LBYL -> if operation not in operations_map, print error
                if operation not in operations_map:
                    print(f"Unknown operation '{operation}'. Type 'help' for instructions.")
                    continue

                # instantiates appropriate calculation class based on the 3 parts passed in
                # dynamic -> strategy pattern
                # lets us get rid of if statements checking for operations
                calculation = operations_map[operation].create(a, b)

                # perform calculation and store result in variable
                result = calculation.compute()

                # print result
                print(f"Result: {result}")

            # EAFP -> perform operation and handle exceptions afterwards
            except ZeroDivisionError:
                print("Error: Division by zero.")
            # if input cannot be converted into floats
            except ValueError:
                print("Invalid numbers. Please enter valid numeric values.")
            # catch any other exception not listed
            except Exception as e:
                print(f"An error occurred: {e}")

# checks if this script is being run as the main program and not as a module
if __name__ == '__main__':
    main()
