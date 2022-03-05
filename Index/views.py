from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenidos al foro de Agus<h1>')


def plantilla(request):
    
    template = loader.get_template('plantillas.html')
    
    datos = {
        'lista':['1','2','3'],
        'profesion':'Contador Publico'
    }
    
    plantilla_generada = template.render({})
    
    return HttpResponse(plantilla_generada)




