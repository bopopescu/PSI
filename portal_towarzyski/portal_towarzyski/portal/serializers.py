from .models import zainteresowania_uzytkownika, Dane_uzytkownika
from rest_framework import serializers

class zainteresowania_uzytkownika_Serializer(serializers.Serializer):
    class Meta:
        model = zainteresowania_uzytkownika
        fields = '__all__'


class Dane_uzytkownika_Serializer(serializers.Serializer):
    class Meta:
        model = Dane_uzytkownika
        fields = '__all__'