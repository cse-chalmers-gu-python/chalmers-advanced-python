"""
more property-based tests, for a function which computes the greatest common divisor
"""

from hypothesis import given
from hypothesis import strategies as st

def gcd(a: int, b: int) -> int:
    """Return greatest common divisor of two ints"""
    while b != 0:
    # while b > 1: # 🐞
        a, b = b, a % b
    return abs(a)

@given(st.integers(min_value=1), st.integers(min_value=1)) # "give me two random integers"
def test_divides_both(a: int, b: int):
    d = gcd(a, b) # call test function
    assert a % d == 0 # assert as usual
    assert b % d == 0

@given(st.integers(), st.integers())
def test_commutative(a: int, b: int):
    assert gcd(a, b) == gcd(b, a)

@given(st.integers(), st.integers())
def test_non_negative(a, b):
    assert gcd(a, b) >= 0

@given(st.integers())
def test_same_number(a):
    assert gcd(a, a) == abs(a)

if __name__ == "__main__":
    test_divides_both()
    test_commutative()
    test_non_negative()
    test_same_number()
