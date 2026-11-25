def first(names: list[str]) -> str | None:
    """Return first name from list, sorted alphabetically"""
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    order = {ch: i for i, ch in enumerate(alphabet)}
    if names:
        return sorted(names, key=lambda word: order.get(word[0], -1))[0]

import unittest
class FirstTest(unittest.TestCase):
    def test_animals(self):
        self.assertEqual(first(["fish","dog","cat"]), "cat")

    def test_empty_list(self):
        self.assertEqual(first([]), None)

    def test_djur(self):
        self.assertEqual(first(["örn","älg","åsna"]), "åsna")

    def test_DJUR(self):
        self.assertEqual(first(["ÖRN","ÄLG","ÅSNA"]), "ÅSNA")

    def test_empty_string(self):
        self.assertEqual(first(["", "fish"]), "fish")

    def test_numbers1(self):
        self.assertEqual(first(["2", "10", "4"]), "2")

    def test_numbers2(self):
        self.assertEqual(first(["4", "10", "2"]), "2")

    def test_spaces(self):
        self.assertEqual(first(["fish","  dog","cat"]), "cat")

if __name__ == "__main__":
    unittest.main()

# ok NOW surely we've thought of all edges cases... RIGHT? 😰
