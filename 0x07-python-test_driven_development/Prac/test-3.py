#!/usr/bin/python3
import unittest, example

class TesExample(unittest.TestCase):
    def test_greet_person(self):
        greeting_message = example.greet_person('Joe')
        self.assertEqual(greeting_message, "Welcome Joe")
    
    def test_greet_person_lowercase(self):
        self.assertEqual(example.greet_person('joe'), "Welcome Joe")



if __name__ == "__main__":
    unittest.main()
