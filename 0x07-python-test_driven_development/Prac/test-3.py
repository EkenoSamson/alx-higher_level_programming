#!/usr/bin/python3
import unittest, example

class TesExample(unittest.TestCase):
    def test_greet_person(self):
        greeting_message = example.greet_person('Joe')
        self.assertEqual(greeting_message, "Welcome Joe")
