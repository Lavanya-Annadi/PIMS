import json

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from .models import savelink_org
# Create your views here.
@csrf_exempt
def addlink(request):
    if request.method == 'POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        print(type(var3))
        url = var3.get('url')
        title = var3.get('title')
        tags = var3.get('tags')
        labels = var3.get('labels')
        b = savelink_org(url = url,title=title,tags = tags,labels = labels)
        b.save()
        return JsonResponse({"status":"link saved"})
def getorganiser(request):
    if request.method == 'GET':
        list_org=list(savelink_org.objects.values())
        return JsonResponse(list_org,safe=False)

def searchorg(request):
    pass
@csrf_exempt
def dellink(request):
    if request.method == 'POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        print(type(var3))
        url = var3.get('url')
        savelink_org.objects.filter(url=url).delete()
        return JsonResponse({'status':'ok'})

def changeread(request):
    if request.method == 'POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        print(type(var3))
        url = var3.get('url')
        read_status= var3.get('read_status')
        savelink_org.objects.filter(url=url).update(read_status=read_status)
        return JsonResponse({'status':'updated readstatus'})

def changescore(request):
    if request.method=='POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        print(type(var3))
        url = var3.get('url')
        score = var3.get('score')
        savelink_org.objects.filter(url=url).update(score=score)
        return JsonResponse({'status':'updated score'})

