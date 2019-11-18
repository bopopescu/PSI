# Stwórz nowy moduł w projekcie o nazwie . Stwórz klasę FileManager z parametrem w konstruktorze file_name. Klasa będzie zawierać dwie metody: read_file oraz update_file. Funkcja update_file powinna zawierac parametr text_data, które w efekcie ma być dopisane na końcu pliku. Funkcja read_file powinna zwrócić zawartość pliku.file_manager

from PSi_3.file_manager import FileManager

plik = FileManager('zad8')
plik.read_file()
tekst = " ...dalszy tekst"
plik.update_file(tekst)
plik.read_file()