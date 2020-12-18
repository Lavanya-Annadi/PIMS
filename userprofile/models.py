from django.db import models
# Create your models here.
class Profile(models.Model):
    username=models.CharField(max_length=250,default="user")
    email=models.CharField(max_length=250,default="email")
    pistack=models.TextField(default='Intrests')

    # def __str__(self):
    #     return f"{self.username} with {self.email} has {self.pistack}"




