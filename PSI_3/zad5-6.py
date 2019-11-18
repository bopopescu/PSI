# Stwórz klasę ScienceCalculator, która dziedziczy po klasie Calculator i dodaj dodatkowe funkcje np. potęgowanie.

from PSi_3.zad5 import Calculator

class ScienceCalculator(Calculator):
    def exponentiation(self):
        return self.a ** self.b