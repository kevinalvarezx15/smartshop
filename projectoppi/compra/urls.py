from argparse import Namespace
from django.urls import path
from . import views

app_name = 'compra'
urlpatterns =[
    path('',views.CompraListView.as_view(), name='compra'),
    path('Crear/',views.CompraCreateView.as_view(), name='crearCompra'),
    path('update/<int:pk>',views.CompraUpdateView.as_view(),name='updCompra')
   
    
]