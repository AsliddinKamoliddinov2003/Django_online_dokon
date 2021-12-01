from django.db import models
from accounts.models import User


class ClientProfile(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client")
    image = models.ImageField(upload_to="images/", null=True)
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.account.first_name