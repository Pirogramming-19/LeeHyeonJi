from django.shortcuts import render, redirect
from .models import Idea
from .forms import DevtoolForm

def main(request):
    ideas = Idea.objects.all()
    return render(request, 'myApp/main.html', {'ideas':ideas})

def search_all_devtool():
    pass

def search_devtool(request, pk):
    pass

def create_devtool(request):
    if request.method == 'POST':
        form = DevtoolForm(request.POST)
        if form.is_valid():
            idea = form.save()
            return redirect('search_devtool', pk = idea.id)
    else:
        form = DevtoolForm()
    return render(request, 'myApp/create_devtool.html', {'form':form})

def update_devtool():
    pass

def delete_devtool():
    pass