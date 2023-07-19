from django.shortcuts import render, redirect
from .models import Idea, Devtool, IdeaStar
from .forms import IdeaForm, DevtoolForm

def main(request):
    ideas = Idea.objects.all()
    return render(request, 'myApp/main.html', {'ideas':ideas})

def main_interest(request, pk, incdec):
    idea = Idea.objects.get(id = pk)
    if incdec == 'inc':
        idea.interest += 1
    elif incdec == 'dec':
        idea.interest -= 1
    idea.save()
    return redirect('/')

def main_starred(request, onoff, pk):
    if onoff == 'staron':
        idea = Idea.objects.get(id = pk)
        IdeaStar.objects.create(idea = idea)
    elif onoff == 'staroff':
        idea = Idea.objects.get(id = pk)
        ideaStar = IdeaStar.objects.filter(idea = idea)
        ideaStar.delete()
    return redirect('/')

def search_idea(request, pk):
    idea = Idea.objects.get(id = pk)
    return render(request, 'myApp/search_idea.html', {'idea':idea})

def create_idea(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect('search_idea', pk = idea.id)
    else:
        form = IdeaForm()
    return render(request, 'myApp/create_idea.html', {'form':form})

def update_idea(request, pk):
    idea = Idea.objects.get(id = pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
            return redirect('search_idea', pk = idea.id)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'myApp/update_idea.html', {'form':form})

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
            devtool = form.save()
            return redirect('search_devtool', pk = devtool.id)
    else:
        form = DevtoolForm()
    return render(request, 'myApp/create_devtool.html', {'form':form})

def update_devtool(request, pk):
    devtool = Devtool.objects.get(id = pk)
    if request.method == 'POST':
        form = DevtoolForm(request.POST, instance=devtool)
        if form.is_valid():
            devtool = form.save()
            return redirect('search_devtool', pk = devtool.id)
    else:
        form = DevtoolForm(instance=devtool)
    return render(request, 'myApp/update_devtool.html', {'form':form})

def delete_devtool(request, pk):
    devtool = Devtool.objects.get(id = pk)
    devtool.delete()
    return redirect('/devtool/')