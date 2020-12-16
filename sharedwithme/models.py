from django.db import models
from collection.models import collection
# Create your models here.
class sharedwithme(models.Model):
    username=models.CharField(max_length=50)
    collection=models.OneToOneField(collection,on_delete=models.CASCADE)