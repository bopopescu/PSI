# Stwórz funkcję, która jako parametry przyjmuje dwie listy a_list oraz b_list. Następnie zwróć listę, która będzie posiadać parzyste indeksy z listy a_list oraz nieparzyste z b_list.

a_list = [4,5,3,2,5,6]
b_list = [2,3,4,5,6,7]

for index, wartosc in enumerate(a_list):
    if index%2==0:
        nowa_lista=[wartosc]
        print(nowa_lista)


for index2, wartosc2 in enumerate(b_list):
    if index2%2==1:
        nowa_lista2=[wartosc2]
        print(nowa_lista2)


