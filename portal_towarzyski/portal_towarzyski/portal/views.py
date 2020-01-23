from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .models import Zainteresowania, Dane_uzytkownika, Znajomi
from .serializers import Zainteresowania_uzytkownika_Serializer, Dane_uzytkownika_Serializer, Znajomi_Serializer
from django.template import loader



# Create your views here.
def index(request):
    template = loader.get_template('muzeumApp/index.html')
    return HttpResponse(template.render({}, request))


class ZnajomiLista(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = Znajomi.objects.all()
    serializer_class = Znajomi_Serializer

    def get(self, request):
        prac = Znajomi.objects.all()
        serializer = Znajomi_Serializer(prac, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Znajomi_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ZnajomiDetail(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = Znajomi.objects.all()
    serializer_class = Znajomi_Serializer

    def get(self, request, pk):
        prac = Znajomi.objects.filter(id=pk)
        serializer = Znajomi_Serializer(prac, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        prac = Znajomi.objects.filter(id=pk)
        prac.delete()


class ZainteresowaniaLista(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = Zainteresowania.objects.all()
    serializer_class = Zainteresowania_uzytkownika_Serializer

    def get(self, request):
        prac = Zainteresowania.objects.all()
        serializer = Zainteresowania_uzytkownika_Serializer(prac, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Zainteresowania_uzytkownika_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ZainteresowaniaDetail(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = Zainteresowania.objects.all()
    serializer_class = Zainteresowania_uzytkownika_Serializer

    def get(self, request, pk):
        prac = Zainteresowania.objects.filter(id=pk)
        serializer = Zainteresowania_uzytkownika_Serializer(prac, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        prac = Zainteresowania.objects.filter(id=pk)
        prac.delete()


class Dane_uzytkownikaLista(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = Dane_uzytkownika.objects.all()
    serializer_class = Dane_uzytkownika_Serializer

    def get(self, request):
        prac = Dane_uzytkownika.objects.all()
        serializer = Dane_uzytkownika_Serializer(prac, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Dane_uzytkownika_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Dane_uzytkownikaDetail(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = Dane_uzytkownika.objects.all()
    serializer_class = Dane_uzytkownika_Serializer

    def get(self, request, pk):
        prac = Dane_uzytkownika.objects.filter(id=pk)
        serializer = Dane_uzytkownika_Serializer(prac, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        prac = Dane_uzytkownika.objects.filter(id=pk)
        prac.delete()

