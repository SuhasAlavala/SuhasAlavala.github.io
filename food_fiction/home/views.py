from django.shortcuts import render


def home(request):
    context = {
        'foods': food.objects.all()
    }	

    return render(request, 'home/homepage.html', context)