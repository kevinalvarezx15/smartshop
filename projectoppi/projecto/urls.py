from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('',views.cargar_login, name='login'),
    path('logout',views.LogoutRedirectView.as_view(), name='logout'),
    path('registro/',views.cargar_registro, name='registro'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="projecto/resetpassword.html"), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="projecto/mensajeresetenviado.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="projecto/confirmacionresetpass.html"),name='password_reset_complete'),


    
]




