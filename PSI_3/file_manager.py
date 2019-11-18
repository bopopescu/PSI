# Stwórz nowy moduł w projekcie o nazwie . Stwórz klasę FileManager z parametrem w konstruktorze file_name. Klasa będzie zawierać dwie metody: read_file oraz update_file. Funkcja update_file powinna zawierac parametr text_data, które w efekcie ma być dopisane na końcu pliku. Funkcja read_file powinna zwrócić zawartość pliku.file_manager

class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        file = open(self.file_name, 'r')
        print(file.read())
        file.close()

    def update_file(self, text_data):
        file = open(self.file_name, 'a')
        file.write(text_data,)
        file.close()