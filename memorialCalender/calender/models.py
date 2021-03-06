from django.db import models
from django.contrib.auth.models import User

class Calender(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=20, null=False)
    start_day = models.DateField()
    # cycle_with
    # 0 : day
    # 1 : week
    # 2 : month
    # 3 : year
    # cycle_with = models.CharField(max_length=5)
    cycle_with = models.PositiveSmallIntegerField()
    cycle_unit = models.IntegerField()