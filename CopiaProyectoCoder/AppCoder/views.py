from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Cursor
from django.template import loader
def cursor(self):
    curso = Cursor(nombre = 'Desarrollo web', camada = 1234563)
    curso.save()
    documento =  f'curso: {curso.nombre} - camada: {curso.camada}'
    return HttpResponse(documento)
# Create your views here.
def inicio(request):
    return HttpResponse("vista inicio")

def cursos(request):
    return HttpResponse("vista cursos")

def profesores(resquest):
    return HttpResponse("vista profesores")

def estudiantes(request):
    return HttpResponse("vista estudiantes")

def entregables(request):
    return HttpResponse("vista entregables")

def mi_plantilla(self):
    plantilla = loader.get_template('plantilla.html')
    documento=plantilla.render()
    return HttpResponse(documento)