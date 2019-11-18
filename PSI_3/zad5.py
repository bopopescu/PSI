# Stwórz klasę Calculator, która będzie posiadać funkcje add, difference, multiply, divide.

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a +self.b

    def difference(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b
