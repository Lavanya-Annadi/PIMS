import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import ast
from django.contrib.auth.hashers import make_password,check_password
from .models import User
from django.http import JsonResponse, HttpResponse
from userprofile.models import Profile

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        print(type(var3))
        username = var3.get('username')
        email = var3.get('email')
        Password = var3.get('password')
        print("userdetails", username, email, Password)
        User.objects.create_user(username=username, email=email, password=Password)
        Profile.objects.create(username=username,email=email)
        return JsonResponse({'status': 'ok created'})
@csrf_exempt
def letmein(request):
    if request.method=='POST':
        var1 = request.body
        var2 = var1.decode('UTF-8')
        var3 = json.loads(var2)
        print(var2)
        print(var1)
        print(type(var3))
        email = var3.get('email')
        Password = var3.get('password')
        val2 = {}
        # print("userdetails", email, Password)
        # y=list(User.objects.filter(email=email).values())[0]
        # pasval=y["password"]
        # print("pasval",pasval)
        # x=check_password(Password,pasval)
        # print(x)
        x=authenticate(email=email,password=Password)
        if x is not None:
          val2["username"]=x.username
          return JsonResponse(val2,safe=False)
        else:
            return JsonResponse({"status":"Login failed"})

