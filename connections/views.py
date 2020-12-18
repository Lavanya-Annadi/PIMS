from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import connection
# Create your views here.
from organiser.Helperfunctions import list_conv,byte_dict_conv
@csrf_exempt
def my_connections(request):
    if request.method=='GET':
        username=request.GET["username"]
        val=connection.objects.filter(username=username).values()
        i=list_conv(val)[0]
        dict1={}
        del i["pending_users"]
        i = i["connected_users"].split(",")
        dict1["connections"]=i
        return JsonResponse(dict1,safe=False)
@csrf_exempt
def pending_connections(request):
    if request.method=='GET':
        username=request.GET["username"]
        val=connection.objects.filter(username=username).values()

        i = list_conv(val)[0]

        dict1 = {}
        del i["connected_users"]
        i = i["pending_users"].split(",")
        dict1["Pending_connections"] = i
        return JsonResponse(dict1, safe=False)
@csrf_exempt
def search_connections(request):
    if request.method=='GET':
        var1=request.body


@csrf_exempt
def connect(request):
    if request.method=='POST':
        var1=request.body
        var2=byte_dict_conv(var1)
        sender=var2.get("username")
        receiver = var2.get("conn_receiver")
        query_val=list(connection.objects.filter(username=receiver).values())[0]
        query_val['pending_users']+=f",{sender}"
        connection.objects.filter(username=receiver).update(pending_users=query_val['pending_users'])
        return JsonResponse({"status":"request sent"})

@csrf_exempt
def accept(request):

    if request.method=='POST':
        a=request.body
        val1=byte_dict_conv(a)
        username= val1.get("username")
        sender= val1.get("sender")
        #update username
        conn=list(connection.objects.filter(username=username).values())[0]
        conn['connected_users'] += f",{sender}"
        connection.objects.filter(username=username).update(connected_users=conn['connected_users'])
        connection.objects.filter(username=username)
        var2=conn["pending_users"].split(",")
        var2.remove(sender)
        var3=",".join(var2)
        connection.objects.filter(username=username).update(pending_users=var3)
        #update sender
        conn = list(connection.objects.filter(username=sender).values())[0]
        conn['connected_users'] += f",{username}"
        connection.objects.filter(username=sender).update(connected_users=conn['connected_users'])

        return JsonResponse({"status":"user connected"})

@csrf_exempt
def disconnect(request):
    if request.method=='POST':
        values=request.body
        val1 = byte_dict_conv(values)
        username = val1.get("username")
        sender = val1.get("sender")
        # connection.objects.filter(username=username)
        conn = list(connection.objects.filter(username=username).values())[0]
        var2 = conn["connected_users"].split(",")
        var2.remove(sender)
        var3 = ",".join(var2)
        connection.objects.filter(username=username).update(connected_users=var3)

        conn = list(connection.objects.filter(username=sender).values())[0]
        var2 = conn["connected_users"].split(",")
        var2.remove(username)
        var3 = ",".join(var2)
        connection.objects.filter(username=sender).update(connected_users=var3)
        return JsonResponse({"status":"connection removed"})
