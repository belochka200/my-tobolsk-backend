from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class UserManager(AbstractBaseUser):
    name = models.CharField("Name", max_length=255)
    password = models.CharField("Password", max_length=24)