import pytest
import pexpect
import sys

@pytest.fixture
def repl():
    """Fixture to start the REPL application."""
    # Path to the main.py script
    script = 'main.py'

    # Start the REPL application
    child = pexpect.spawn(sys.executable + f' {script}', encoding='utf-8', timeout=5)
    child.expect('Welcome to the Calculator REPL.*')
    yield child
    child.terminate()

def test_repl_addition(repl):
    """Test addition operation in the REPL."""
    repl.sendline('add 10 5')
    repl.expect('Result: 15\.0')
    repl.sendline('exit')
    repl.expect('Goodbye!')

def test_repl_help(repl):
    """Test the help command in the REPL."""
    repl.sendline('help')
    repl.expect('Available commands:')
    repl.sendline('exit')
    repl.expect('Goodbye!')

def test_repl_invalid_command(repl):
    """Test handling of an unknown command."""
    repl.sendline('unknown 1 2')
    repl.expect("Unknown operation 'unknown'.*")
    repl.sendline('exit')
    repl.expect('Goodbye!')

def test_repl_division_by_zero(repl):
    """Test division by zero handling."""
    repl.sendline('divide 10 0')
    repl.expect('Error: Division by zero\.')
    repl.sendline('exit')
    repl.expect('Goodbye!')

def test_repl_invalid_numbers(repl):
    """Test handling of invalid numeric input."""
    repl.sendline('add ten five')
    repl.expect('Invalid numbers\. Please enter valid numeric values\.')
    repl.sendline('exit')
    repl.expect('Goodbye!')

def test_repl_multiple_operations(repl):
    """Test multiple operations in a single REPL session."""
    repl.sendline('add 1 2')
    repl.expect('Result: 3\.0')
    repl.sendline('subtract 5 3')
    repl.expect('Result: 2\.0')
    repl.sendline('multiply 4 2')
    repl.expect('Result: 8\.0')
    repl.sendline('divide 9 3')
    repl.expect('Result: 3\.0')
    repl.sendline('exit')
    repl.expect('Goodbye!')

def test_repl_show_history(repl):
    """Test showing history."""
    repl.sendline('add 1 2')
    repl.expect('Result: 3\.0')
    repl.sendline('history')
    repl.expect('1: Addition')
    repl.sendline('exit')
    repl.expect('Goodbye!')

def test_repl_undo(repl):
    """Test undo functionality."""
    repl.sendline('add 3 4')
    repl.expect('Result: 7\.0')
    repl.sendline('undo')
    repl.expect('Undid operation: Addition')
    repl.sendline('exit')
    repl.expect('Goodbye!')

def test_repl_clear_history(repl):
    """Test clearing history."""
    repl.sendline('add 2 3')
    repl.expect('Result: 5\.0')
    repl.sendline('clear')
    repl.expect('History cleared.')
    repl.sendline('history')
    repl.expect('The history is empty!')
    repl.sendline('exit')
    repl.expect('Goodbye!')
