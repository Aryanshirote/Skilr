from django.urls import path
from accounts.views import *

urlpatterns = [
    path('',home, name ="home"),
    path("login/", login, name="login"), 
    path("dasboard", dashboard, name ="dashboard"),    
    path("register/", register, name="register"),
    path("file_upload/", file_upload, name="file_upload"),
    # path('about/', views.about, name="about_us")
]