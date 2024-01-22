from django.urls import path
from .views import *

app_name = "post"

urlpatterns = [
    path('', show_main, name='main_page'),
    path('like/', mark_like, name='mark_like'),
    path('comment/create/', create_comment, name='create_comment'),
    path('comment/delete/', delete_comment, name='delete_comment'),
    path('post/create/', create_post, name='create_post')
]
