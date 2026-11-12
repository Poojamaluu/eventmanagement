from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    role_choices = [('organizer','Organizer'),
                    ('customer','Customer')]
    role = models.CharField(choices=role_choices,max_length=20)
    phone = models.CharField(max_length=20)