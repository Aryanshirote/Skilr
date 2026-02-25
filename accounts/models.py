from django.db import models

class Registrations(models.Model):
    username = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    password = models.CharField(null=False)
    cnfm_password = models.CharField(null=False)



