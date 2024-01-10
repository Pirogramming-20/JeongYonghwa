from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list')
]

# mysite.urls -> blog.urls로 전송요청 전파
# 이때 경로는 둘다 ''->''이므로, 
# 기본 주소 요청 = post_list에 대한 요청