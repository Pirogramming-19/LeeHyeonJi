from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name="main"),
    path('idea/order/<str:std>/', main_ordered, name="main_ordered"),
    path('idea/<int:pk>/<str:incdec>/', main_interest, name="main_interest"),
    path('idea/<str:onoff>/<int:pk>/', main_starred, name="main_starred"),
    path('idea/<int:pk>/', search_idea, name="search_idea"),
    path('idea/create/', create_idea, name="create_idea"),
    path('idea/<int:pk>/update/', update_idea, name="update_idea"),
    path('idea/<int:pk>/delete/', delete_idea, name="delete_idea"),
    path('devtool/', search_all_devtool, name="search_all_devtool"),
    path('devtool/<int:pk>/', search_devtool, name="search_devtool"),
    path('devtool/create/', create_devtool, name="create_devtool"),
    path('devtool/<int:pk>/update/', update_devtool, name="update_devtool"),
    path('devtool/<int:pk>/delete/', delete_devtool, name="delete_devtool"),
]