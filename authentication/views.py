from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# from dashboard.models import Profile
# from dashboard.models import Bulletin


def index(request):
    return render(request, 'base.html')


# print(request)


"""def dashboard(request):
   if not request.user.username == 'chintu':
       return HttpResponse("unauthorised")
   return HttpResponse("<h1>dashboard<h1>")





def adminlogin(request):
   return HttpResponse("response admin login")


@login_required(login_url="/login")
def edit_profile(request):
   if request.method == 'POST':
       user = request.user
       pistack = request.POST['pistack']
       profile, created = Profile.objects.get_or_create(user=request.user)
       user.profile.pistack = pistack
       user.save()
   return render(request, 'edit.html')


@login_required(login_url='/admin/login')
def dashboard(request):
   if request.method == 'POST':
       body = request.POST.get('body')
       bulliten = Bulletin()
       bulliten.body = body
       bulliten.save()
   if request.user is None or not request.user.is_staff:
       return HttpResponse("unauthorized")
   return render(request, 'admindash.html')"""

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


"""def register(request):
    if request.method == 'POST':
        print("post method representation" + request.scheme)
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if username == '': return HttpResponse("No username")
        if password == '': return HttpResponse("No password")
        if email == '': return HttpResponse("no email")
        User.objects.create_user(username=username, password=password, email=email)
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse("unauthorized")
        else:
            login(request, user)
            return redirect('/')
            return HttpResponse('your username is : ' + username)

    return render(request, 'signup.html')
"""

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("username",username)
        print("password",password)
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse('unauthorized')
        else:
            login(request, User)
            return redirect('home')
            return HttpResponse('your username is : ' + username)
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return HttpResponse("successfully logged out")


def home(request):
    return redirect('home.html')
