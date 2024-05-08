import unittest
import sympy as sp

class Function:
    def __init__(self, expression):
        self.expression = expression
        self.symbol = sp.Symbol('x')
        self.function = sp.sympify(expression)

    def calculate_derivative(self):
        derivative = sp.diff(self.function, self.symbol)
        return derivative

class TestFunction(unittest.TestCase):
    def test_derivative(self):
        # Teste simples com função linear
        func = Function("2*x + 3")
        expected_derivative = "2"
        self.assertEqual(str(func.calculate_derivative()), expected_derivative)

        # Teste com função quadrática
        func = Function("x**2 + 2*x + 1")
        expected_derivative = "2*x + 2"
        self.assertEqual(str(func.calculate_derivative()), expected_derivative)

if __name__ == "__main__":
    unittest.main()
