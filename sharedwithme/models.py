from django.db import models
from collection.models import collection
# Create your models here.
class sharedwithme(models.Model):
    username=models.CharField(max_length=50,default='username')
    sender=models.CharField(max_length=50,default='sender')
    collection=models.ForeignKey(collection,on_delete=models.CASCADE)