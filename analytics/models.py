from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    file = models.FileField(upload_to="resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)

    skills = models.TextField(blank=True)
    education = models.TextField(blank=True)

    score = models.IntegerField(default=0)

    extracted_text = models.TextField(blank=True)