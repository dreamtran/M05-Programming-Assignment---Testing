import unittest
from fractions import Fraction
from my_sum import sum

# Unit tests for the sum function
class TestSum(unittest.TestCase):
    # Test case: summing a list of integers
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
    
    # Test case: summing a list of fractions
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)
    
    # Test case: handling an invalid input type
    def test_bad_type(self):
        """
        Test that it raises a TypeError for an invalid input type
        """
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)
            
if __name__ == '__main__':
    unittest.main()