from django.db import models

class FacebookUser(models.Model):
    facebook_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    gender = models.CharField(max_length=6)
