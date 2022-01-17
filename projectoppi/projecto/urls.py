from django.urls import path
from . import views

urlpatterns =[
    path('login/',views.cargar_login, name='login'),
    path('registro/',views.cargar_registro, name='registro'),
    
]




