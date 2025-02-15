"""PIMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from authentication import views
#from mysite.core import views
from searchengine import views as v
from collection import views as collect_v
from organiser import views as org_v
from Users import views as user_v
from sharedwithme import views as share_v
from userprofile import views as prof_v
from connections import views as conn_v
from trends import views as trend_v
urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index),
    path('login',user_v.letmein),
    path('home',views.home),
    path('signup',user_v.signup),
    path('logout',views.logout_user),
    path('search',v.searchresult),
    #"""organiser Urls"""
    path('addToOrganiser',org_v.addlink),
    path('saveOrganiser',org_v.addlink),
    path('organiserLinks',org_v.getorganiser),
    path('organiser',org_v.getorganiser),
    path('deleteorgLink',org_v.dellink),
    path('searchOrganiser',org_v.searchorg),
    path('saveReadStatus',org_v.changeread),
    path('saveScore',org_v.changescore),
    #"""collections urls"""
    path('collections', collect_v.getcollection),
    path('collectionsNames', collect_v.getcollection),
    path('createCollection',collect_v.createcoll),
    path('saveCollection',collect_v.updatecoll),
    path('deleteCollection',collect_v.deletecoll),
    path('deleteLink',collect_v.delrow),
    path('saveRank',collect_v.updaterank),
    path('shareCollection',collect_v.sharecoll),
    path('searchUsers',collect_v.searchuser),
    #"""profile"""
    path('profile',prof_v.getprofile),

#connections
    path('getMyConnections',conn_v.my_connections),
    path('getPendingConnections',conn_v.pending_connections),
    path('searchConnections',conn_v.search_connections),
    path('connectUser',conn_v.connect),
    path('disconnectUser',conn_v.disconnect),
    path('accept',conn_v.accept),
    #shared
    path('getSharedWithMeDetails',share_v.getshareddetails),
    #trends
    path('trends',trend_v.gettrends)
]
