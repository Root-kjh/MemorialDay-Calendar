from django.db import models
from user.models import User

class Calender(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    start_day = models.DateField()
    cycle_with = models.CharField(max_length=5)
    cycle_unit = models.IntegerField()