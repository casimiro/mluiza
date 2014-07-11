from django.db import models

class FacebookUser(models.Model):
    facebookId = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    gender = models.CharField(max_length=6)
