from django.shortcuts import render
from django.http import HttpResponse
from .models import Poem

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
