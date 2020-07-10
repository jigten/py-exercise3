import unittest
from roman import convert_to_roman

class RomanTest(unittest.TestCase):
    # Check a small integer convertion
    def test_small_integer(self):
        output_1 = convert_to_roman(3)
        self.assertEqual(output_1, "III")

    # Check an exact conversion
    def test_exact_integer(self):
        output_2 = convert_to_roman(900)
        self.assertEqual(output_2, "CM")

    # Check a large integer conversion
    def test_large_integer(self):
        output_3 = convert_to_roman(4350)
        self.assertEqual(output_3, "MMMMCCCL")

if __name__ == '__main__':
    unittest.main()