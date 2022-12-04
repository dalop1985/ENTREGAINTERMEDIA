from django.urls import path
from Familia.views import *

urlpatterns = [
 #   path('tios/', tios),
 #   path('hermano/', herm),
 #   path('prim/', prim),
 #   path('viven/', viven),
 #   path('trab/', trab),
    path('',inicio, name="Inicio"),
    path('Familia_tios/',Familia_tios, name="Tios"),
    path('Familia_hermanos/',Familia_hermanos, name="Hermanos"),
    path('Familia_primos/',Familia_primos, name="Primos"),
    path('Familia_lugar/',Familia_lugar, name="Lugar"),
    path('Familia_trabajan/',Familia_trabajan, name="Trabajan"),
    path('BFamilia_tios/',BFamilia_tios, name="BFamilia_tios" ),
    path('Btios/',Btios, name="Btios"),
    path('BFamilia_hermanos/',BFamilia_hermanos, name="BFamilia_hermanos" ),
    path('BFamilia_primos/',BFamilia_primos, name="BFamilia_primos" ),
    path('BFamilia_lugar/',BFamilia_lugar, name="BFamilia_lugar" ),
    path('BFamilia_trabajan/',BFamilia_trabajan, name="BFamilia_trabajan" ),
    path('Bhermanos/',Bhermanos, name="Bhermanos"),
    path('Bprimos/',Bprimos, name="Bprimos"),
    path('Blugar/',Blugar, name="Blugar"),
    path('Btrabajan/',Btrabajan, name="Btrabajan"),
]
