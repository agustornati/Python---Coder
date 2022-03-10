from django.urls import path
from .views import index 

urlpatterns = [
   path('', index, name='index'),
   #path('indice-2/', index, name='indice_2')
]
