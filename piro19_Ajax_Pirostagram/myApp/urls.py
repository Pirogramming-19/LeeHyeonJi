from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name="main"),
    path('like_ajax/', like_ajax, name="like_ajax"),
    path('leave_comment_ajax/', leave_comment_ajax, name="leave_comment_ajax"),
    path('remove_comment_ajax/', remove_comment_ajax, name="remove_comment_ajax"),
]
