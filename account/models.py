from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from .manager import CustomUserManager



class User(AbstractUser):
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to="profile")
    

    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


