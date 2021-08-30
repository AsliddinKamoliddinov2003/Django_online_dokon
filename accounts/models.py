from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager, PermissionsMixin


class UserManager(UserManager):
    def create_user(self,gmail,password=None):
        user = self.model(gmail=gmail)
        user.set_password(password)
        user.save()

        return user

    
    def create_superuser(self, gmail, password):
        user = self.create_user(gmail,password)
        user.is_admin = True
        user.is_superuser = True
        user.save()

        return user




class User(AbstractBaseUser, PermissionsMixin):
    gmail = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    GENDERS = {
        ("m", "male"),
        ("f", "female")
    }
    genders = models.CharField(choices=GENDERS, max_length=10, default="m")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_seperuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = "gmail"
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def has_perm(self, obj):
        return self.is_admin

    
    def has_module_perms(self, add_label):
        return True

