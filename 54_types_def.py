'''

In Python, typing refers to type hints or type annotations—a way to explicitly specify the types of variables, function arguments, and return values to improve code clarity, readability, and tooling support (like auto-completion or error detection in editors).

'''

from typing import List, Tuple, Dict, Union, Optional, Any
n : int = 5

name : str = "Amal"


def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."


# union means it can hold multiple types
def divide(x: int, y: int) -> Union[float, str]:
    if y == 0:
        return "Cannot divide by zero"
    return x / y

