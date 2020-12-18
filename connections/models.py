from django.db import models


# Create your models here.
from django.utils import timezone


class connection(models.Model):
    username = models.CharField(max_length=200, default='username')
    connected_users = models.TextField()
    pending_users = models.TextField()
    def __str__(self):
        return f"{self.username} connected  {self.connected_users} and pending {self.pending_users}"


