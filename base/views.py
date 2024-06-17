from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Poem
from .forms import PoemForm

# Create your views here.

def home(request):
    # Objects is a manager that allows us to interact with the database
    # all() is a method that returns all the objects in the database
    # get() is a method that returns a single object that matches the query
    # filter() is a method that returns a list of objects that match the query
    # exclude() is a method that returns a list of objects that don't match the query
    poems = Poem.objects.all()
    context = {
        'poems': poems
    }
    return render(request, 'base/home.html', context)

def poem(request, pk):
    poem = Poem.objects.get(id=pk)
    context = {
        'poem': poem
    }
    return render(request, 'base/poem.html', context)

def createPoem(request):
    form = PoemForm()
    if request.method == 'POST':
        form = PoemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/poem_form.html', context)

def updatePoem(request, pk):
    poem = Poem.objects.get(id=pk)
    # with instance=poem, we are telling the form to update a specific poem
    form = PoemForm(instance=poem)
    # save the updated form
    if request.method == 'POST':
        form = PoemForm(request.POST, instance=poem)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    # render the form
    context = {'form': form}
    return render(request, 'base/poem_form.html', context)