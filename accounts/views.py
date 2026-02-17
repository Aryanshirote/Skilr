from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login



def home(request):
    return render (request, 'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "admin" and password == "admin":
            return render (request, 'home.html')
        else:
            return render (request, 'login.html', {"error": "Invalid username or password"})
    return render (request, 'login.html')

def dashboard(request):
    return render (request, 'dashboard.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # Here you would typically save the user to the database
        return render (request, 'login.html', {"message": "Registration successful. Please log in."})
    return render (request, 'register.html')


