from argparse import Namespace
from django.urls import path
from . import views

app_name = 'cliente'
urlpatterns =[
    path('',views.ClienteListView.as_view(), name='cliente'),
    path('Crear/',views.ClientesCreateView.as_view(), name='crearCliente'),
    path('Editar/<int:pk>',views.ClienteUpdateView.as_view(), name='EditarCliente'),
    path('cb/',views.selectCliente, name='selectCliente'),
    path('Eliminar/<int:pk>',views.ClienteDeleteView.as_view(), name='EliminarCliente'),
    #path('registro/<int:pk>/',views.ClienteUpdateView.as_view(), name='registro'),
    
]




