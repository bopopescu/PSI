from .models import Zainteresowania, Dane_uzytkownika, Znajomi, Znajomi_has_zainteresowania_uzytkownik
from rest_framework import serializers

class Zainteresowania_uzytkownika_Serializer(serializers.Serializer):
    class Meta:
        model = Zainteresowania
        fields = '__all__'

class Dane_uzytkownika_Serializer(serializers.Serializer):
    class Meta:
        model = Dane_uzytkownika
        fields = '__all__'


class Znajomi_Serializer(serializers.Serializer):
    class Meta:
        model = Znajomi
        fields = '__all__'

class Znajomi_has_zainteresowania_uzytkownik_Serializer(serializers.Serializer):
    class Meta:
        model = Znajomi_has_zainteresowania_uzytkownik
        fields = '__all__'



