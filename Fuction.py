import sympy as sp

class Function:
    def __init__(self, expression):
        self.expression = expression
        self.symbol = sp.Symbol('x')
        self.function = sp.sympify(expression)

    def calculate_derivative(self):
        derivative = sp.diff(self.function, self.symbol)
        return derivative

def main():
    expression = input("Digite a função (em termos de x): ")
    func = Function(expression)
    derivative = func.calculate_derivative()
    print(f"A derivada da função é: {derivative}")

if __name__ == "__main__":
    main()
