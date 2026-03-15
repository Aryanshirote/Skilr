from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Registrations


# -------------------------------------------------------
# REGISTER VIEW
# -------------------------------------------------------
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cnfm_password = request.POST.get("confirm_password")
        if password !=cnfm_password:
            msgstr = {"error" : "Passwords do not match"}
            return render (request, "register.html", msgstr)
        else:
            if User.objects.filter(username=username, email=email).exists():
                return render(request,"register.html", {"bothtaken": "Username and E-mail is already taken "})
            elif User.objects.filter(email=email).exists():
                return render (request, "register.html", {"emailtaken": "Email id has been registered already Please login"})
            elif User.objects.filter(username=username).exists():
                return render (request, "login.html", {"usertaken": "Username is already taken"})
            user = User.objects.create_user(
                username = username,
                email = email,
                password = password
            
            )
            user.save()
        
        return redirect('login')
        
    return render (request, 'register.html')

# -------------------------------------------------------
# LOGIN VIEW
# -------------------------------------------------------

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard') 
        else:
            return render(request, 'login.html', {"error": "Invalid username or password"})
    return render(request, 'login.html')
# -------------------------------------------------------
# LOGOUT VIEW
# -------------------------------------------------------
@login_required
def logout_view(request):
    logout(request)
    return redirect("home")






