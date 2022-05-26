from django.urls import path
from AppCoder.views import cursos, profesores
from AppCoder.views import mi_plantilla

urlpatterns = [
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('mi_plantilla/', mi_plantilla)
]