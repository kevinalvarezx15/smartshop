from django.urls import path
from . import views

urlpatterns =[
    path('',views.cargar_cliente, name='cliente'),
    path('Crear',views.addnew, name='crearCliente'),
    path('Editar/<int:id>/<var:nombre:>',views.editCliente, name='EditarCliente'),
    # path('registro/',views.cargar_registro, name='registro'),
    
]




