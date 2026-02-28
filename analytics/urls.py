from django.contrib import admin
from django.urls import path, include
from accounts import urls
from analytics.views import *


urlpatterns = [
    path("fileupload/", file_upload, name="file_upload"),

]
