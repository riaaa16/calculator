'''importing calculation class and number typehinting'''
from typing import List, Union
from app.calculation import Calculation
from app.operations import Number

class OperationCommand:
    '''pattern for executing operations'''
    # initializes OperationCommand by defining the operation
    def __init__(self, operation: Calculation) -> None:
        self.operation = operation

    def execute(self) -> Number:
        '''returns result of operation'''
        return self.operation.compute()

class HistoryManager:
    '''
    Manages history of executed operations.

    You can add to, retrieve, or undo from the history of operations.
    Stores a list of 'OperationCommand' objects representing each calculation.

    _history(List[OperationCommand]): shows list of operations executed
    '''

    def __init__(self) -> None:
        '''initializes historyManager with the empty history list'''
        self._history: List[OperationCommand] = []

    # type hinting that operation is of Class OperationCommand
    def add_to_history(self, operation: 'OperationCommand') -> None:
        '''
        appends new operation to history list
        '''
        self._history.append(operation)

    def get_latest(self, n: int = 1) -> List['OperationCommand']:
        '''
        get the latest n operations from the history

        n should be an int, and the default value is 1
        '''
        return self._history[-n:]

    def clear_history(self) -> None:
        '''clears the history'''
        self._history.clear()

    def get_full_history(self) -> List['OperationCommand']:
        '''
        returns entire operation history
        '''
        return self._history

    def undo_last(self) -> Union['OperationCommand', None]:
        '''
        pops the last command from history list
        
        returns nothing if the history is empty
        '''
        if self._history:
            return self._history.pop()
        return None
    