def plus(a, b):
    return a + b

import unittest
class TestQuiz(unittest.TestCase):
    def test_q1(self):
        self.assertGreater(plus(3, 6), 9)

    def test_q2(self):
        self.assertFalse(plus(3, 6) > 9)

    def test_q3a(self):
        self.assertEqual(plus(0.3, 0.6), 0.9)

unittest.main()
