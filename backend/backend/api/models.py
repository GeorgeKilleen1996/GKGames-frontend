from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name=None, last_name=None, admin=False):
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, admin=admin)
        user.set_password(password)
        user.save(using=self._db)
        return user

# Create your models here.

class User(AbstractBaseUser):
    objects = UserManager()

    email = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
