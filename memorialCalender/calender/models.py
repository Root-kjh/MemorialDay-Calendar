from django.db import models
from user.models import User

class Calender(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=20, null=False)
    start_day = models.DateField()
    cycle_with = models.CharField(max_length=5)
    cycle_unit = models.IntegerField()