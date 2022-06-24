
from django.shortcuts import render

# Create your views here.

# routing the html files here
def index(request):
    return render(request, 'home/index.html')


def aboutUs(request):
    return render(request, 'home/about.html')

def school(request):
    return render(request, 'home/homepage.html')