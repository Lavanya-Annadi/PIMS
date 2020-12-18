import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import collection, row
from organiser.Helperfunctions import list_conv, byte_dict_conv
from sharedwithme.models import sharedwithme

# Create your views here.
@csrf_exempt
def getcollection(request):
    if request.method == 'GET':
        username=request.GET["username"]
        values=collection.objects.filter(username=username).values()
        print(values)
        if list(values)==[]:
            return JsonResponse([{"status":"no collections"}],safe=False)
        else:
            collections_list=list_conv(values)

            return JsonResponse(collections_list, safe=False)

@csrf_exempt
def createcoll(request):
    if request.method == 'POST':
         var1 = request.body
         values=byte_dict_conv(var1)
         username=values.get("username")
         title = values.get('name')
         coll = collection(name=title,username=username)
         coll.save()
         return JsonResponse({"STATUS": "SAVED COLLECTION"})

@csrf_exempt
def updatecoll(request):
    if request.method == 'POST':
        var1 = request.body
        print("var1 values",var1)
        var2=var1.decode('UTF-8')
        print(var2)
        var3=json.loads(var2)
        print(type(var3))
        username=var3.get('username')
        title = var3.get('name')
        list_links = var3.get('links')
        coll_name = collection.objects.filter(name=title,username=username)
        d1=list(coll_name)[0]
        for i in list_links:
            url = i.get('url')
            row.objects.create(collname=d1, url=url)

        return JsonResponse({"STATUS": "SAVED rows"})

@csrf_exempt
def deletecoll(request):
    if request.method == 'POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        username=var3.get('username')
        name = var3.get('Title')
        collection.objects.filter(username=username,name=name).delete()
        return JsonResponse({'status': 'deleted the collection'})

@csrf_exempt
def sharecoll(request):
    if request.method == 'POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        name = var3.get('title')
        user = var3.get('username')
        sender=var3.get('sender')
        d1=list(collection.objects.filter(username=sender,name=name))[0]
        sharedwithme.objects.create(username=user,sender=sender,collection=d1)
        return JsonResponse({"status":"shared collection"})

@csrf_exempt
def searchuser(request):
    pass


def updaterank(request):
    pass

@csrf_exempt
def delrow(request):
    if request.method == 'POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        title=var3.get('Title')
        username = var3.get('username')
        url=var3.get('url')
        coll1=collection.objects.filter(username=username,name=title)
        l1=list(coll1)[0]
        print(l1)
        print(row.objects.filter(collname=l1,url=url))
        row.objects.filter(collname=l1,url=url).delete()
        return JsonResponse({'status': 'deleted the collection'})
