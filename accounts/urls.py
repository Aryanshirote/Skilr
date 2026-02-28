from django.urls import path
from accounts.views import *

urlpatterns = [
    path('',home, name ="home"),
    path("login/", login, name="login"), 
    path("dasboard", dashboard, name ="dashboard"),    
    path("register/", register, name="register"),
    path("logout/", logout_view, name="logout"),
]