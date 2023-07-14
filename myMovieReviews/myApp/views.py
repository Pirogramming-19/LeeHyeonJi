from django.shortcuts import render, redirect
from .models import Review
from django.http.request import HttpRequest

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'myApp/review_list.html', {'reviews':reviews})

def review_detail(request, pk):
    review = Review.objects.get(id = pk)
    time = review.running_time
    return render(request, 'myApp/review_detail.html', 
                {'review':review, 'running_hour':time//60, 'running_min':time%60})

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

def review_update(request: HttpRequest, pk):
    review = Review.objects.get(id = pk)

    if request.method == 'POST':
        review.title = request.POST['title']
        review.release_year = request.POST['release_year']
        review.genre = request.POST['genre']
        review.rate = request.POST['rate']
        review.running_time = request.POST['running_time']
        review.content = request.POST['content']
        review.director = request.POST['director']
        review.lead = request.POST['lead']
        review.save()
        return redirect(f'/review/{review.id}/')

    return render(request, 'myApp/review_update.html', {'review':review})