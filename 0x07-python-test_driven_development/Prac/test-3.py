#!/usr/bin/python3
import unittest, example

class TesExample(unittest.TestCase):
    def test_greet_person(self):
        with self.subTest():
            greeting_message = example.greet_person('Joe')
            self.assertEqual(greeting_message, "Welcome Joe")

        with self.subTest():
            self.assertEqual(example.greet_person('joe'), "Welcome Joe")

    def test_can_drink_alcohol(self):
        """ Test if he/she can drink alcohol """
        self.assertTrue(example.can_drink_alcohol(21))



if __name__ == "__main__":
    unittest.main()
