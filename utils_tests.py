#python lib that gives us tools for writing automated tests
# can automatically tell us pass or fail 
import unittest
from utils import utils

class UtilsTests(unittest.TestCase):

    def test_reversed_integer(self):
        u = utils()
        self.assertEqual(u.reversed(1234), 4321)

    def test_reversed_string(self):
        u = utils()
        with self.assertRaises(TypeError):
            u.reversed("1234")

    def test_reversed_float(self):
        u = utils()
        with self.assertRaises(TypeError):
            u.reversed(12.34)

    def test_formatter_integer(self):
        u = utils()
        self.assertEqual(u.formatter(10), ("0b1010", "0o12"))

    def test_formatter_string(self):
        u = utils()
        with self.assertRaises(TypeError):
            u.formatter("10")

    def test_formatter_float(self):
        u = utils()
        with self.assertRaises(TypeError):
            u.formatter(10.5)

if __name__ == "__main__":
    unittest.main()