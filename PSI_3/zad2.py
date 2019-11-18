#Stwórz funkcję, która przyjmuje parametr data_text, a następnie zwróci następujące informacje o parametrze w formie słownika (dict):
#    length: długość podanego tekstu,
#   letters: lista znaków w wyrazie np. ['D', 'o', 'g'],
#    big_letters: zamieniony parametr w kapitaliki np. DOG
#   small_letters: zamieniony parametr w małe litery np. dog

def info(data_text):
    slownik = {}
    lenght = len(data_text)
    slownik["Dlugosc: "] = lenght
    letters = list(data_text)
    slownik["Lista liter: "] = letters
    big_letters = data_text.upper()
    slownik["Z wilkich liter: "] = big_letters
    small_letters = data_text.lower()
    slownik["Z małych liter: "] = small_letters
    print(slownik)

wyraz = "fHJasd"
print(info(wyraz))