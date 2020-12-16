import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import collection, row


# Create your views here.
def getcollection(request):
    if request.method == 'GET':
        coll_list = list(collection.objects.values())
        return JsonResponse(coll_list, safe=False)


def createcoll(request):
    if request.method == 'POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        print(type(var3))
        title = var3.get('title')
        coll = collection(name=title)
        coll.save()
        return JsonResponse({"STATUS": "SAVED COLLECTION"})


def updatecoll(request):
    if request.method == 'POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        print(type(var3))
        title = var3.get('title')
        list_links = var3.get('links')
        coll_name = collection.objects.filter(name=title)
        for i in list_links:
            url = i.get('url')
            row.objects.create(collname=coll_name, url=url)
        return JsonResponse({"STATUS": "SAVED rows"})


def deletecoll(request):
    if request.method == 'POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        name = var3.get('title')
        collection.objects.filter(name=name).delete()
        return JsonResponse({'status': 'deleted the link'})


def sharecoll(request):
    if request.method == 'POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        name = var3.get('title')
        user = var3.get('username')


def searchuser(request):
    pass


def updaterank(request):
    pass


def delrow(request):
    pass
