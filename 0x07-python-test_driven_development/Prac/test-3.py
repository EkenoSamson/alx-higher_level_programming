#!/usr/bin/python3
import unittest, example

class TesExample(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        " Beginning"
        print("Starting test cases")

    def setUp(self):
        """ Run before every test """
        print("Set Up")

    def tearDown(self):
        """" After every test """
        print("Tear Down")

    def test_greet_person(self):
        with self.subTest('Uppercase J'):
            greeting_message = example.greet_person('Joe')
            self.assertEqual(greeting_message, "Welcome Joe")

        with self.subTest('Lowercase j'):
            self.assertEqual(example.greet_person('joe'), "Welcome Joe")

    def test_can_drink_alcohol(self):
        """ Test if he/she can drink alcohol """
        with self.subTest():
            self.assertTrue(example.can_drink_alcohol(21))
        with self.subTest():
            self.assertFalse(example.can_drink_alcohol(16))

    @classmethod
    def tearDownClass(cls):
        """ Ending """
        print(" Ending test cases")



if __name__ == "__main__":
    unittest.main()

