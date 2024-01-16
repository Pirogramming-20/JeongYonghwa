from django.urls import path
from .views import *

app_name = 'idea'

urlpatterns = [
    path('', show_list, name='main_page'),
    path('idea/create/', create, name='create'),
    path('idea/detail/<int:pk>', detail, name='detail'),
    path('idea/delete/<int:pk>', delete, name='delete'),
    path('idea/update/<int:pk>', update, name='update'),
    path('idea/change_marked/<int:pk>', change_marked, name='change_marked'),
]