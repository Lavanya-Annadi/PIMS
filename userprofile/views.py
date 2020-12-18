from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from userprofile.models import Profile
from organiser.Helperfunctions import byte_dict_conv
@csrf_exempt
def getprofile(request):
    if request.method == 'GET':
        query = request.GET['username']
        search_resp = list(Profile.objects.filter(username=query).values())[0]
        del search_resp['id']
        return JsonResponse(search_resp, safe=False)

    if request.method=='POST':
        value=request.body
        resultval = byte_dict_conv(value)
        pistack=resultval.get("pistack")
        username=resultval.get("username")
        Profile.objects.filter(username=username).update(pistack=pistack)
        return JsonResponse({"status":"updated PISTACK"})


