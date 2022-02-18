from django.urls import path
from . import views

urlpatterns =[
    path('',views.cargar_login, name='login'),
    path('registro/',views.cargar_registro, name='registro'),
    
]




