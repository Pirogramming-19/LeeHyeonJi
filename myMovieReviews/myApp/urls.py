from django.urls import path, include
from .views import *

urlpatterns = [
    path('', review_list),
]