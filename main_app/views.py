from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cat

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')


cats = [
    Cat("Lolo", "tabby", "foul little demon", 3),
    Cat("Sachi", "tortoise shell", "diluted tortoise shell", 0),
    Cat("Raven", "black tripod", "3 legged cat", 4),
]


def cats_index(request):
    return render(request, 'cats/index.html', {'cats': cats})