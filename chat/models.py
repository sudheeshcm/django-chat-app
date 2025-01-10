from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)

class Message(models.Model):
    text = models.CharField(max_length=1000)
    room_id = models.IntegerField(null=True)
    user_name = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=datetime.now, blank=True)