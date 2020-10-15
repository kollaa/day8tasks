import unittest
import unit

class FactTest(unittest.TestCase):
    def test_factorial(self):
        result = unit.factor(3)
        self.assertEquals(result, 8)
    
    def test_factorial1(self):
        result = unit.factor(3)
        self.assertEquals(result, 6)


if __name__ == '__main__':
    unittest.main()