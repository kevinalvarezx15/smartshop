from argparse import Namespace
from django.urls import path
from . import views

app_name = 'tipoproductos'
urlpatterns =[
    path('',views.TipoProductoListView.as_view(), name='tipoproducto'),
    path('Crear/',views.TipoProductoCreateView.as_view(), name='crearTipoproducto'),
    path('Editar/<int:pk>',views.TipoProductoUpdateView.as_view(), name='EditarTipoproducto'),
    path('Eliminar/<int:pk>',views.TipoProductoDeleteView.as_view(), name='EliminarTipoproducto'),
    
]




