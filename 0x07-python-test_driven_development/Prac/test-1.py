#!/usr/bin/python3
# import library
import unittest


# create a class
class TestXXXX(unittest.TestCase):
    #define a function
    def test_xxxx(self):
        data = [100, 200, 300]
        result = sum(data)
        self.assertEqual(result, 6000)

# driver code
if __name__ == "__main__":
    unittest.main()
