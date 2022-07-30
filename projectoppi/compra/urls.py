from argparse import Namespace
from django.urls import path
from . import views

app_name = 'compra'
urlpatterns =[
    path('',views.CompraListView.as_view(), name='compra'),
    path('Crear/',views.CompraCreateView.as_view(), name='crearCompra'),
    #path('Editar/<int:pk>',views.ClienteUpdateView.as_view(), name='EditarCliente'),
    #path('cb/',views.selectCliente, name='selectCliente'),
    #path('Eliminar/<int:pk>',views.ClienteDeleteView.as_view(), name='EliminarCliente'),
    #path('registro/<int:pk>/',views.ClienteUpdateView.as_view(), name='registro'),
    
]