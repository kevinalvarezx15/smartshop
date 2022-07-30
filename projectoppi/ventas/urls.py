from argparse import Namespace
from django.urls import path
from . import views
app_name = 'ventas'
urlpatterns =[
    path('',views.VentaListView.as_view(), name='ventas'),
    path('Crear/',views.VentaCreateView.as_view(), name='crearVenta'),
]