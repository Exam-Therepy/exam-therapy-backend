import datetime
from datetime import timezone

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from user.manager import MainUserManager


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MainUser(AbstractBaseUser, PermissionsMixin):
    username = None
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, null=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    full_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    payment_id = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(null=False, default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['mobile', 'full_name']
    objects = MainUserManager()

    def __str__(self):
        return self.full_name
