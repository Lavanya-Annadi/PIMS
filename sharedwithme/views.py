from django.http import JsonResponse
from django.shortcuts import render
from .models import  sharedwithme
# Create your views here.
from organiser.Helperfunctions import list_conv


def getshareddetails(request):
    if request.method=='GET':
        username=request.GET['username']
        getdetails=sharedwithme.objects.filter(username=username).values()
        values=list_conv(getdetails)
        if values==[]:
            return JsonResponse({"Status":"none shared"})
        else:
            for i in values:
                del i["id"]
            return JsonResponse(values,safe=False)


