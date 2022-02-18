from django.urls import path
from . import views

app_name = 'proveedores'
urlpatterns =[
    path('',views.ProvedoresListView.as_view(), name='proveedores'),
    path('crear',views.ProveedorCreateView.as_view(), name='crearProveedor'),
    path('cb/',views.selectProveedores, name='selectProveedores'),
    path('Editar/<int:pk>',views.ProveedoresUpdateView.as_view(), name='EditarProveedor'),
    path('Eliminar/<int:pk>',views.ProveedorDeleteView.as_view(), name='EliminarProveedor'),
   
    # path('registro/',views.cargar_registro, name='registro'),
]
    