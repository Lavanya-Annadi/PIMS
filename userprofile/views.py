from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from userprofile.models import Profile

@csrf_exempt
def getprofile(request):
    if request.method == 'GET':
        query = request.GET['username']
        search_resp = list(Profile.objects.filter(username=query).values())[0]
        del search_resp['id']
        return JsonResponse(search_resp, safe=False)
def setprofile(request):
    pass
