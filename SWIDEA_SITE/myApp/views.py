from django.shortcuts import render
from .models import Idea

def main(request):
    ideas = Idea.objects.all()
    return render(request, 'myApp/main.html', {'ideas':ideas})
