import function_for_test
import unittest


class TestIsPair(unittest.TestCase):
    def test_is_pair(self):
        self.assertTrue(function_for_test.is_pair(2))
        self.assertFalse(function_for_test.is_pair(1))
        self.assertEqual(function_for_test.is_pair(0), True)


if __name__ == '__main__':
    unittest.main()
