from argparse import Namespace
from django.urls import path
from . import views

app_name = 'inventario'
urlpatterns =[
    path('',views.InventarioListView.as_view(), name='inventarioV'),
    
]