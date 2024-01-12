from django.urls import path
from .views import *

urlpatterns = [
    path('', review_list, name="review_list"),
    path('review/<int:pk>/detail/', review_detail, name="review_detail"),
    path('review/create/', review_new, name="review_create"),
    path('review/<int:pk>/update/', review_update, name="review_update"),
    path('review/<int:pk>/delete/', review_delete, name="review_delete"),
    path('review/<str:criteria>/order',review_order, name="review_order")
]