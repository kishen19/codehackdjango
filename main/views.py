from django.http import JsonResponse
from .models import hospital
import mpu
from django.views.decorators.csrf import csrf_exempt

def dist(x1, y1, x2, y2):
    return mpu.haversine_distance((x1, y1), (x2, y2))


def sort(x, y, l):
    dis = []
    for i in l:
        dis.append([dist(x, y, i.x, i.y), i.name, i.x, i.y, i.address, i.status])
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

@csrf_exempt
def handle(request):
    try:
        x = float(request.POST.get('lati'))
        y = float(request.POST.get('longi'))
        hospitals = hospital.objects.all()
        final = sort(x, y, hospitals)
        print('Data Received')
        return JsonResponse({0:final})
    except:
        print('Did not receive data')
        return JsonResponse({})