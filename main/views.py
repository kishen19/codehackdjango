from django.shortcuts import render,HttpResponse

from .models import hospital



def index(request):
    return render(request, 'main.html', {})


def handle(request):
    locationx = 0
    locationy = 0
    hospitals = hospital.objects.all()

    print(hospitals)