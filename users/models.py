from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username
