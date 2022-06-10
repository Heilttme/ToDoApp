from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class CustomAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, password=password)
        user.save()

        return user


class UserToDo(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    completed_todos = models.IntegerField(default=0)
    left_todos = models.IntegerField(default=0)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomAccountManager()

    def __str__(self):
        return self.username
