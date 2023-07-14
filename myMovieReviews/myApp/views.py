from django.shortcuts import render
from .models import Review

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'myApp/review_list.html', {'reviews':reviews})