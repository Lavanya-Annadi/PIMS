from django.db import models

# Create your models here.
from django.db import models


# Create your models here.


class savelink_org(models.Model):
    username=models.CharField(max_length=250,null=True)
    url=models.CharField(max_length=500,null=True)
    title = models.CharField(max_length=100,null=True)
    labels = models.CharField(max_length=100,null=True)
    tags = models.CharField(max_length=200,null=True)
    read_status = models.BooleanField(null=True,default=False)
    score = models.IntegerField(null = True,default=0)
    created=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        if self.title == None:

            return ''
        return self.title

