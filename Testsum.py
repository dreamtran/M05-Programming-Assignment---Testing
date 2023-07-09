# Pytest unit tests for the sum function

def test_sum():
    # Test case: summing a list
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    # Test case: summing a tuple
    assert sum((1, 2, 2)) == 6, "Should be 6"