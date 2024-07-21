from typing import Union

def add(first, second) -> int:
    """Add two numbers together."""
    return first + second

def subtract(first, second) -> int:
    """Subtract the second number from the first."""
    return first - second

def multiply(first, second) -> int:
    """Multiply two numbers together."""
    return first * second

def divide(first, second) -> Union[int, str]:
    """Divide the first number by the second."""
    if second != 0:
        return first / second
    else:
        return 'Division by zero error'
