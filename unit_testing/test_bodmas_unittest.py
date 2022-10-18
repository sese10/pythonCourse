import bodmas
import unittest

class TestBodmas(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(bodmas.addition(3, 1), 4)
        self.assertEqual(bodmas.addition(20, 1), 21)
        self.assertEqual(bodmas.addition(-2, -1), -3)

    def test_subtraction(self):
        self.assertEqual(bodmas.subtraction(3, 1), 2)
        self.assertEqual(bodmas.subtraction(10, 5), 5)

if __name__ == '__main__':
    unittest.main()

