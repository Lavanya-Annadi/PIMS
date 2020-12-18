import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from organiser.models import savelink_org

def gettrends(request):
    if request.method=='GET':
        time_24_hours_ago = datetime.datetime.now() - datetime.timedelta(days=1)
        value=savelink_org.objects.filter(created__gte=time_24_hours_ago).values()
        print('value',value)
        list_val=list(value)
        print('list_val',list_val)
        x=[]
        for i in list_val:
            dic_val={}
            title=i.get('title')
            url=i.get('url')
            dic_val['title']=title
            dic_val['url']=url
            x.append(dic_val)

        return JsonResponse(x,safe=False)