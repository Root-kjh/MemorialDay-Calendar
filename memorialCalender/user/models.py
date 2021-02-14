from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length = 20, unique=True)
    user_password = models.CharField(max_length=128)