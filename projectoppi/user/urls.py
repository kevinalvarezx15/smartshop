from django.urls import path
from user.views import *
from . import views

app_name = 'user'

urlpatterns = [
    # user
    path('', UserListView.as_view(), name='user_list'),
    path('CrearUser/',views.UserCreateView.as_view(), name='crearUser'),
    path('EditarUser/<int:pk>',views.UserUpdateView.as_view(), name='EditarUser'),
    path('EliminarUser/<int:pk>',views.UserDeleteView.as_view(), name='EliminarUser'),

]