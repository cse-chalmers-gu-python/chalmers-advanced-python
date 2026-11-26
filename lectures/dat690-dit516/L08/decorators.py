# decorators, and how they decorate other functions 

from typing import Callable

        # Callable [ [list of parameters], return_type ]
def decorator(func: Callable[ [int], int]) -> Callable[ [int], str]: 
    def decorate(param: int) -> str:
        ans = func(param)
        # print(f'ans is {ans}')
        return f'ans is {ans}'

    return decorate 

@decorator
def make_square(n: int) -> int:
    return n**2

def make_cube(n: int) -> int:
    return n**3

print(make_cube(5))
print(make_square(8))


# decorator(make_cube) (6)  # manual way of decorating a function 
# decorator(make_square) (8)




# func      --> function's name or memory id 
# func()     --> execute that function with name func