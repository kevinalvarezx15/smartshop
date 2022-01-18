from django.urls import path
from . import views

urlpatterns =[
    path('',views.cargar_productos, name='productos'),
    path('Crear',views.addnew, name='crear'),
    path('CreaTipo',views.addnewTipoProducto, name='crearTipo'),
    path('TipoProducto',views.cargar_TipoProducto, name='tipoProducto'),

    # path('registro/',views.cargar_registro, name='registro'),
    
]




