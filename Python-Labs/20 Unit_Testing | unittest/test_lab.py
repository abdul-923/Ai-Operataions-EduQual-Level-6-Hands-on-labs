

def add(a, b):
 return a + b

import unittest

class TestMath(unittest.TestCase):
 def test_add(self):
   self.assertEqual(add(2, 3), 5)
