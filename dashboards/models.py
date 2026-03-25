from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):

    CATEGORY_CHOICES = [
        ("bug", "Bug Report"),
        ("feature", "Feature Request"),
        ("general", "General Feedback"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="general"
    )

    rating = models.IntegerField(choices=[(i, i) for i in range(1,6)])

    message = models.TextField()

    screenshot = models.ImageField(upload_to="feedback/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} : \n {self.message}"