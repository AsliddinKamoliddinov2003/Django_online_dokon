from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager, PermissionsMixin


class UserManager(UserManager):
    def create_user(self,email,password=None):
        user = self.model(email=email)
        user.set_password(password)
        user.save()

        return user

    
    def create_superuser(self, email, password):
        user = self.create_user(email,password)
        user.is_admin = True
        user.is_superuser = True
        user.save()

        return user




class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255,unique=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    GENDERS = {
        ("m", "male"),
        ("f", "female")
    }
    gender = models.CharField(choices=GENDERS, max_length=10, default="m", null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def has_perm(self, obj):
        return self.is_admin

    
    def has_module_perms(self, add_label):
        return True

