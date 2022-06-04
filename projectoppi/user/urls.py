from django.urls import path
from user.views import *

app_name = 'user'

urlpatterns = [
    # user
    path('list/', UserListView.as_view(), name='user_list'),

]