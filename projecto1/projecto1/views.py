from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
def saludo(request):
    return HttpResponse('Hola mundo')
def view_dos(request):
    return HttpResponse('Segundaview')

def probandoTemplate(self):
    nombre = 'Samuel'
    apellido = 'Pianeta'
    notas = [1,2,3,4,5,6,7,8,9]
    diccionario = {'nombre':nombre, 'apellido':apellido, 'notas':notas}
    #miHtml = open('Template1.html')

    #plantilla = Template(miHtml.read())
    #miHtml.close()

    #miContexto = Context(diccionario)
    plantilla = loader.get_template('Template1.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
