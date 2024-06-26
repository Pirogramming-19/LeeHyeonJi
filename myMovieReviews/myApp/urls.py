from django.urls import path, include
from .views import *

urlpatterns = [
    path('', review_list),
    path('review/<int:pk>/', review_detail),
    path('review/<int:pk>/delete/', review_delete),
    path('review/create/', review_create),
    path('review/<int:pk>/update/', review_update),
    path('<int:pk>/', review_order),
]