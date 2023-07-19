from django.shortcuts import render, redirect
from .models import Idea, Devtool
from .forms import DevtoolForm

def main(request):
    ideas = Idea.objects.all()
    return render(request, 'myApp/main.html', {'ideas':ideas})

def search_idea(request, pk):
    idea = Idea.objects.get(id = pk)
    return render(request, 'myApp/search_idea.html', {'idea':idea})

def create_idea():
    pass

def update_idea():
    pass

def delete_idea(request, pk):
    idea = Idea.objects.get(id = pk)
    idea.delete()
    return redirect('/')

def search_all_devtool(request):
    devtools = Devtool.objects.all()
    return render(request, 'myApp/search_all_devtool.html', {'devtools':devtools})

def search_devtool(request, pk):
    devtool = Devtool.objects.get(id = pk)
    ideas = devtool.idea.all()
    return render(request, 'myApp/search_devtool.html', {'devtool':devtool, 'ideas':ideas})

def create_devtool(request):
    if request.method == 'POST':
        form = DevtoolForm(request.POST)
        if form.is_valid():
            idea = form.save()
            return redirect('search_devtool', pk = idea.id)
    else:
        form = DevtoolForm()
    return render(request, 'myApp/create_devtool.html', {'form':form})

def update_devtool(request, pk):
    devtool = Devtool.objects.get(id = pk)
    if request.method == 'POST':
        form = DevtoolForm(request.POST, instance=devtool)
        if form.is_valid():
            idea = form.save()
            return redirect('search_devtool', pk = idea.id)
    else:
        form = DevtoolForm(instance=devtool)
    return render(request, 'myApp/update_devtool.html', {'form':form})

def delete_devtool(request, pk):
    devtool = Devtool.objects.get(id = pk)
    devtool.delete()
    return redirect('/devtool/')