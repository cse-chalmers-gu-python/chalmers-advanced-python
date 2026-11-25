"""
a decorator is really just a function
which takes a function as an argument
and returns another function
which wraps the original function
🤯
"""

from typing import Callable

def debug(function: Callable[[int], int]):
    def wrapper(x: int):
        ans = function(x)
        print(f"{function.__name__} applied to {x} returns {ans}")
        return function
    return wrapper

@debug
def double(x: int) -> int:
    return x * 2

# alternative to using @debug:
# double = debug(double)

double(5)
