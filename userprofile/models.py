from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

import Users
from Users import models as usermodel


class Profile(models.Model):
    user=models.OneToOneField(Users,on_delete=models.CASCADE)
    Pistack=models.TextField(default='Intrests')

"""@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()"""


