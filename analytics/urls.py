from django.contrib import admin
from django.urls import path, include
from accounts import urls
from analytics.views import *


urlpatterns = [
    path("fileupload/", upload_resume, name="file_upload"),
    path("job-match/<int:id>/", job_match, name="job_match"),

]
