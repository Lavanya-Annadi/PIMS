from django.db import models

# Create your models here.


class collection(models.Model):
 username=models.CharField(max_length=250,default="username")
 name = models.TextField()
 def __str__(self):
  return self.name

class row(models.Model):
 collname = models.ForeignKey(collection,on_delete=models.CASCADE)
 url = models.TextField()
 rank = models.IntegerField(default=0)

 def __str__(self):
  return self.url
