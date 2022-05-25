from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Cursor

def cursor(self):
    curso = Cursor(nombre = 'Desarrollo web', camada = 1234563)
    curso.save()
    documento =  f'curso: {curso.nombre} - camada: {curso.camada}'
    return HttpResponse(documento)
# Create your views here.
