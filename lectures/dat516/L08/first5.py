"""
hypothesis is not a relacement for unittest: they work together just fine! 🥰
"""

def first(names: list[str]) -> str | None:
    """Return first name from list, sorted alphabetically"""
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    order = {ch: i for i, ch in enumerate(alphabet)}
    if names:
        return sorted(names, key=lambda word: order.get(word[0], -1))[0]

import unittest
from hypothesis import given, strategies as st
# from hypothesis import settings, Verbosity

class FirstTest(unittest.TestCase):

    @given(st.lists(st.text(min_size=1), min_size=1))
    # @given(st.lists(st.text())) # 🐞
    # @settings(verbosity=Verbosity.verbose)
    def test_returns_member(self, strlist: list[str]):
        f = first(strlist)
        self.assertIn(f, strlist)

    @given(st.lists(st.text(min_size=1, alphabet="abcdefghijklmnopqrstuvwxyzåäö"), min_size=2))
    # @settings(verbosity=Verbosity.verbose)
    def test_returns_less_than(self, strlist: list[str]):
        f = first(strlist)
        if f:
            for s in strlist:
                # self.assertGreater(s, f) # 🐞
                self.assertGreaterEqual(s, f)

if __name__ == "__main__":
    unittest.main()
