from django.shortcuts import render
from .models import Recipe

def home(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'home/home.html', context)


def about(request):
    return render(request, 'home/about.html', {'title': 'About'})
