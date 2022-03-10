from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index/principal.html',{})


# def plantilla(request):
    
    # template = loader.get_template('plantillas.html')
    
    # datos = {
    #     'lista':['1','2','3'],
    #     'profesion':'Contador Publico'
    # }
    
    # plantilla_generada = template.render({})
    
    # return HttpResponse(plantilla_generada)




