# Create your views here.
import json
from django.http import HttpResponse,JsonResponse
from searchengine.search import build_container


def searchresult(request):
    if request.method == 'GET':
        query=request.GET['query']
        search_resp=build_container(query)
        return JsonResponse(search_resp,safe=False)


