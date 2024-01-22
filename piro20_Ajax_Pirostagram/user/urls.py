from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]
