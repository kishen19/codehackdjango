from django.shortcuts import render, HttpResponse
from .models import Person
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def help(request):
    try:
        num = request.POST.get('num')
        locationx = request.POST.get('lati')
        locationy = request.POST.get('longi')
        Person.objects.create(num=num, locationx=locationx, locationy=locationy)
        print('Received data successfully')
        return HttpResponse('ok')
    except:
        print('Did not receive data')
        return HttpResponse('errors')
