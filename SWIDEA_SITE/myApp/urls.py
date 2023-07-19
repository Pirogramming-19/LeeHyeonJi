from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name="main"),
    path('devtool/', search_all_devtool, name="search_all_devtool"),
    path('devtool/<int:pk>/', search_devtool, name="search_devtool"),
    path('devtool/create/', create_devtool, name="create_devtool"),
    path('devtool/<int:pk>/update/', update_devtool, name="update_devtool"),
    path('devtool/<int:pk>/delete/', delete_devtool, name="delete_devtool"),
]