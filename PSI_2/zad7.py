# Połącz te listy ponownie. Dodaj do listy wartość „0” na początku. Utwórz kopię połączonej listy i wyświetl listę posortowaną malejąco.
lista = [1,2,3,4,5,6,7,8,9,10]
nowa_lista=lista[5:10]
lista=lista[0:5]
lista.extend(nowa_lista)

# print(lista)

lista.insert(0, 0)


lista2=lista[:]
print(lista)
lista2.reverse()
print(lista2)