from django.shortcuts import render, redirect
from .models import Review
from django.http.request import HttpRequest

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'myApp/review_list.html', {'reviews':reviews})

def review_detail(request, pk):
    review = Review.objects.get(id = pk)
    return render(request, 'myApp/review_detail.html', {'review':review})

def review_delete(request: HttpRequest, pk):
    if request.method == 'POST':
        review = Review.objects.get(id = pk)
        review.delete()
    return redirect('/')

def review_create(request: HttpRequest):
    if request.method == 'POST':
        Review.objects.create(
            title = request.POST['title'],
            release_year = request.POST['release_year'],
            genre = request.POST['genre'],
            rate = request.POST['rate'],
            running_time = request.POST['running_time'],
            content = request.POST['content'],
            director = request.POST['director'],
            lead = request.POST['lead'],
        )
        return redirect('/')
    return render(request, 'myApp/review_create.html')