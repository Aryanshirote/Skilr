from django.urls import path
from accounts.views import *

urlpatterns = [
    path("login/", login, name="login"), 
    path("register/", register, name="register"),
    path("logout/", logout_view, name="logout"),
]