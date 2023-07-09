import unittest
from my_sum import sum

# Unit tests for the sum function
class TestSum(unittest.TestCase):

    # Test case: summing a list
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    # Test case: summing a tuple
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()