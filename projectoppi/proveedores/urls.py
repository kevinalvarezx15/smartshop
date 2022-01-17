from django.urls import path
from . import views


urlpatterns =[
    path('',views.cargar_proveedores, name='proveedores'),
    path('Crear',views.addnew, name='crearProveedor'),
    # path('registro/',views.cargar_registro, name='registro'),
]
    