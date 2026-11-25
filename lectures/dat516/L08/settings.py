"""
hypothesis can be configured using @settings
"""

from hypothesis import given
from hypothesis import strategies as st
from hypothesis import settings, Verbosity

def double(x):
    return x * 2

@settings(
    verbosity=Verbosity.verbose, # print all values
    max_examples=200 # specify number of examples
)
@given(st.integers())
def test_double_ints(x: int):
    assert double(x) == x + x

if __name__ == "__main__":
    test_double_ints()
