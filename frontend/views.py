from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import ServiceRequest
from django.contrib.auth import get_user_model


def home(request):
    return render(request, "home.html")

User = get_user_model()  

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username, email=email, password=password)
        return redirect("login")

    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "login.html")

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")

    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, "dashboard.html", {"requests": requests})
