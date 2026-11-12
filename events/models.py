from django.db import models
from accounts.models import CustomUser
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()#yyyy-mm-dd
    time = models.TimeField()#hh:mm:ss
    venue = models.CharField(max_length=100)
    amount = models.IntegerField()
    organizer = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)