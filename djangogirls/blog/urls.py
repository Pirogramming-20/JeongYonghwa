from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

# 1. 기본주소/post에서
# 2. 정수로 주어지는 변수 pk의 값을 가질 때
# 3. 해당 요청을 post_detail view로 전송하고
# 4. 그 view는 pk에 적절한 int을 부여하고, 그에 따라 내용을 처리한다

# mysite.urls -> blog.urls로 전송요청 전파
# 이때 경로는 둘다 ''->''이므로, 
# 기본 주소 요청 = post_list에 대한 요청