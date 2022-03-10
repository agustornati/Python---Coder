from django.urls import path
from .views import index, indice_2

urlpatterns = [
   path('', index, name='index'),
   path('indice-2/', index, name='indice_2')
]
