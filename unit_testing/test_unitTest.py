# create a test case that compares two strings
# create another test case that compares different numbers
# use any unit testing framework from this week's lessons.


import unittest
import myTestCase
from myTestCase import main



class testString(unittest.TestCase):
    def test_name(self):
        self.assertEqual(myTestCase.name("Rita"), True)
        self.assertEqual(myTestCase.name("Sandra"), False)  # add assertion here

    def test_upper(self):
        self.assertEqual("Rita" . upper(), "RITA")  # add assertion here
        self.assertEqual("Sandra" . upper(), "SANDRA")

    def test_isupper(self):
        self.assertTrue("RITA" . isupper())  # add assertion here
        self.assertFalse("Sandra" . isupper())

class testNumbers(unittest.TestCase):

    def test_main(self):

       #print("test")
        testList = [1, 2, 5, 9, 0]
        value = main()
        self.assertListEqual(myTestCase.main(), testList)


if __name__ == '__main__':
    unittest.main()
