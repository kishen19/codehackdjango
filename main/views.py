from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from .models import hospital
import mpu
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'update.html',{'hospitals':hospital.objects.order_by('name')})

def supplyindex(request):
    return render(request, 'supply.html',{'hospitals':hospital.objects.order_by('name')})

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
        return JsonResponse({0: final})
    except:
        print('Did not receive data')
        return JsonResponse({})


@csrf_exempt
def entry(request):
    try:
        name = request.POST.get('name')
        addr = request.POST.get('addr')
        x = request.POST.get('lati')
        y = request.POST.get('longi')
        a = hospital(name=name, x=x, y=y, address=addr)
        a.save()
        print('Data recorded successfully')
        return HttpResponse('ok')
    except:
        print('Did not receive data!')
        return HttpResponse('errors')

@csrf_exempt
def submit(request):
    size = len(hospital.objects.all())
    for i in range(1,size+1):
        ans = request.POST.get('button'+str(i))
        if ans=='':
            ans = i
            break
    if type(ans)==int:
        p= hospital.objects.filter(id=i)[0]
        p.status = not p.status
        p.save()
        return index(request)
    else:
        return False
'''
@csrf_exempt
def supply(request):
    size = len(hospital.objects.all())
    for i in range(1, size + 1):
        ans = request.POST.get('button' + str(i))
        if ans == '':
            ans = i
            break
    if type(ans) == int:
        p = hospital.objects.filter(id=i)[0]
        p.status = not p.status
        p.save()
        return index(request)
    else:
        return False'''