"""
a simple demonstration of how hypothesis can
generate random values using strategies
"""

from hypothesis import given
from hypothesis import strategies as st

@given(st.integers()) # "give me a random integer"
def print_num(x: int):
    print(x)

if __name__ == "__main__":
    print_num()
    # we call the function once, without arguments
    # yet it is run multiple times, with many different random values
    # the @given decorator is what does this
