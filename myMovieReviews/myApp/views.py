from django.shortcuts import render
from .models import Review

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'myApp/review_list.html', {'reviews':reviews})

def review_detail(request, pk):
    review = Review.objects.get(id = pk)
    return render(request, 'myApp/review_detail.html', {'review':review})