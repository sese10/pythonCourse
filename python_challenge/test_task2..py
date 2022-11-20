from challenge2 import calculatepower
import unittest


class CalculatePowerTestCase(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculatepower(5, 2), 25)

    if __name__ == '__main__':
        unittest.main()
