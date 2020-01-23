from django.contrib import admin
from django.urls import path
from .. import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('Znajomi', views.ZnajomiLista.as_view()),
    path('Zainteresowania', views.ZainteresowaniaLista.as_view()),
    path('Dane_uzytkownika', views.Dane_uzytkownikaLista.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)