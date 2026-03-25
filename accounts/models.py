from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    INDUSTRY_CHOICES = [
        ("technology", "Technology"),
        ("finance", "Finance"),
        ("management", "Management"),
        ("healthcare", "Healthcare"),
        ("education", "Education"),
        ("arts_design", "Arts_Design"),
        ("retail", "Retail"),
        ("hospitality", "Hospitality"),
        ("law", "Law"),
        ("manufacturing", "Manufacturing"),
    ]

    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)

    def __str__(self):
        return f"{self.user.username}---   Industry: {self.industry}"


