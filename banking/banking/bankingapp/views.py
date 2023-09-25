from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request,"index.html")

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('new')
        else:
            messages.info(req, "Invalid username or password")
            return redirect('login')

    return render(req, "Login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']

        # Check if passwords match
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')  # Redirect to the login page or any other page after successful registration
        else:
            messages.info(request, "Password does not match")
            return redirect('register')
    return render(request, "register.html")


def forms(request):
    return render(request, "forms.html")
def new(request):
    return render(request, "new.html")
