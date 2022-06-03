from argparse import Namespace
from django.urls import path
from . import views

app_name = 'productos'
urlpatterns =[
    path('',views.ProductoListView.as_view(), name='producto'),
    path('CrearProducto/',views.ProductoCreateView.as_view(), name='crearProducto'),
    path('EditarProducto/<int:pk>',views.ProductoUpdateView.as_view(), name='EditarProducto'),
    path('EliminarProducto/<int:pk>',views.ProductoDeleteView.as_view(), name='EliminarProducto'),

    
]




