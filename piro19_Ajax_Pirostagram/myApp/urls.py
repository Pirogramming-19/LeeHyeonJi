from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name="main"),
    path('like_ajax/', like_ajax, name="like_ajax"),
]
