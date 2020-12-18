from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)
# Create your models here.


class Usermanager(BaseUserManager):

    def create_user(self,username,email,password):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an user NAME')


        user = self.model(username = username, email=self.normalize_email(email) )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_staffuser(self, username ,email, password):

        user = self.create_user(username,email, password=password,)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,username, email, password):

        user = self.create_user( username,
                                email,
                                password=password,
                                )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True,db_index=True)
    username = models.CharField(max_length= 100,unique=True,db_index=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = Usermanager()
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):


        return True

    def has_module_perms(self, app_label):


        return True

    @property
    def is_staff(self):

        return self.staff

    @property
    def is_admin(self):

        return self.admin

    @property
    def is_active(self):

        return self.active

