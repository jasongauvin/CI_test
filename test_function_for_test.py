"""
My test is for verified my function "is_pair"
"""
import unittest
import function_for_test

class TestIsPair(unittest.TestCase):
    """
    Test is_pair function
    """
    def test_is_pair(self):
        self.assertTrue(function_for_test.is_pair(2))
        self.assertFalse(function_for_test.is_pair(1))
        self.assertEqual(function_for_test.is_pair(0), True)


if __name__ == '__main__':
    unittest.main()
