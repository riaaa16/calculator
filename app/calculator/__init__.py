'''importing functions from app.operations'''
from typing import List, Union
from app.history import HistoryManager, OperationCommand
from app.operations import addition, subtraction, multiplication, division, Number

class Calculator:
    '''
    Performs operations, manages operation history, and undoes actions
    '''

    def __init__(self) -> None:
        '''
        initializes calculator with a history manager
        creates history manager object
        '''
        self.history_manager = HistoryManager()

    # type hinting that operation should be of the Calculation class
    def perform_operation(self, operation: 'Calculation') -> Number:
        '''
        performs calculation and stores it in history
        
        operation(calculation) = the calculation to perform

        returns the result of the calculation
        '''
        command = OperationCommand(operation)
        result = command.execute()
        self.history_manager.add_to_history(command)
        return result

    def get_history(self) -> List['OperationCommand']:
        '''gets full history of performed operations'''
        return self.history_manager.get_full_history()

    def undo(self) -> Union['OperationCommand', None]:
        '''
        undoes the last operation
        returns none if history is empty
        '''
        return self.history_manager.undo_last()

    def clear_history(self) -> None:
        '''clears entire calculator history'''
        self.history_manager.clear_history()
