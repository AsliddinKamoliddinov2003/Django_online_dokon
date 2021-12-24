from django.db import models
from accounts.models import User


class ClientProfile(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to="images/", null=True)
    phone_number = models.CharField(max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    floor = models.PositiveIntegerField()
    appertment = models.PositiveIntegerField()
    status = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.client.first_name