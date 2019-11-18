# Stwórz funkcję, która przyjmie jako parametry text oraz letter, a następnie zwróci wynik usunięcia wszytkich wystąpień wartości w letter z tekstu text.

def remove(text, letter):
    print(text.replace(letter,""))

tmp = "hahaha"
h = "h"

remove(tmp,h)