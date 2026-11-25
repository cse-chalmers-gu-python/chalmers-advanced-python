"""
property-based test for a function which doubles its argument
"""

from hypothesis import given
from hypothesis import strategies as st

# the function we want to test
def double(x):
    return x * 2

# a test function
@given(st.integers()) # "give me a random integer"
def test_double_ints(x: int):
    # assert double(x) > x # 🐞
    assert double(x) == x + x

if __name__ == "__main__":
    test_double_ints()
