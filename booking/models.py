from datetime import timedelta, datetime
from django.db import models
from events.models import Event
from accounts.models import CustomUser
# Create your models here.
class Booking(models.Model):
    status_choices=[('pending','Pending'),
                    ('confirmed','Confirmed'),
                    ('expired','Expired'),
                    ('cancelled','Cancelled')]
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    seats= models.IntegerField()
    amount = models.IntegerField()
    status = models.CharField(max_length=20,choices=status_choices,default='pending')
    ticket_code=models.CharField(max_length=50,unique=True,null=True,blank=True)#after confirmation we create ticket
    created_at = models.DateTimeField(auto_now_add=True)


    #this function is expiration before making payment
    def check_and_update_expiration(self):
        #Dynamically calculates if 15 minutes have passed since the booking was created.
        #if yes change status to expired.
        booking_time=self.created_at + timedelta(minutes=15)
        if datetime.now() > booking_time:
            self.status = 'expired'
            self.save()
        return self.status