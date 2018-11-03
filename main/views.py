from django.http import JsonResponse
from math import sqrt
from .models import hospital
import mpu

def dist(x1, y1, x2, y2):
    return mpu.haversine_distance((x1, y1), (x2, y2))


def sort(x, y, l):
    dis = []
    for i in l:
        dis.append[[dist(x, y, i.locationx, i.locationy), i.name, i.locationx, i.locationy, i.address, i.status]]
    dis.sort()
    final = []
    for j in dis:
        d = {}
        d['name'] = j[1]
        d['lati'] = j[2]
        d['longi'] = j[3]
        d['addr'] = j[4]
        d['status'] = j[5]
        final.append(d)
    return final


def handle(request):
    x = request.POST.get('lati')
    y = request.POST.get('longi')
    hospitals = hospital.objects.all()
    return JsonResponse(sort(x, y, hospitals))
