import json

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from .Helperfunctions import byte_dict_conv,list_conv
from .models import savelink_org
# Create your views here.
@csrf_exempt
def addlink(request):
    if request.method == 'POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var4 = json.loads(var2)
        var3=var4["organiser"][0]
        print(var2)
        print(var1)
        print(type(var3))
        username = var4.get("username")
        url = var3.get('url')
        title = var3.get('title')
        tags = var3.get('tags')
        labels = var3.get('labels')
        b = savelink_org(username = username,url = url,title=title,tags = tags,labels = labels)
        b.save()
        return JsonResponse({"status":"link saved"})
@csrf_exempt
def getorganiser(request):
    if request.method == 'GET':
        username = request.GET['username']
        queryresult = savelink_org.objects.filter(username= username).values()
        print("queryresult",queryresult)
        list_org = list_conv(queryresult)
        print("list_org",list_org)
        return JsonResponse(list_org,safe=False)
@csrf_exempt
def searchorg(request):
    if request.method == 'GET':
        username=request.GET["username"]
        query=request.GET["query"]
        print('username',username)
        # output1 = list(savelink_org.objects.filter(username=username,labels = query))[0]
        # print("output1", output1)
        # print("link",output1["url"])
        output1=list(savelink_org.objects.filter(username="ram",labels ="info").values())[0]
        # output2 = savelink_org.objects.filter(username=username, tags=query)
        # output3 = savelink_org.objects.filter(username=username, title=query)
        # converted_list= list_conv(output1) + list_conv(output2) + list_conv(output3)
        return JsonResponse(output1,safe=False)




@csrf_exempt
def dellink(request):
    if request.method == 'POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        print(type(var3))
        username = var3.get('username')
        url = var3.get('url')
        savelink_org.objects.filter(username = username,url=url).delete()
        return JsonResponse({'status':'ok'})
@csrf_exempt
def changeread(request):
    if request.method == 'POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        print(type(var3))
        username = var3.get('username')
        url = var3.get('url')
        read_status= bool(var3.get('read_status'))
        savelink_org.objects.filter(username = username,url=url).update(read_status=read_status)
        return JsonResponse({'status':'updated readstatus'})
@csrf_exempt
def changescore(request):
    if request.method=='POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        print(type(var3))
        username = var3.get('username')
        url = var3.get('url')
        score = var3.get('score')
        savelink_org.objects.filter(username = username,url=url).update(score=score)
        return JsonResponse({'status':'updated score'})

