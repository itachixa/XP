import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    # Test pour l'addition
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    # Test pour la soustraction
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 4), -4)
        self.assertEqual(subtract(3, 7), -4)

    # Test pour la multiplication
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    # Test pour la division
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 1), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)  # Teste la division par zéro

if __name__ == '__main__':
    unittest.main()
