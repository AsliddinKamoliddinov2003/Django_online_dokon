from django.db import models
from django.db.models.base import Model




class Category(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    content  = models.TextField()
    image = models.ImageField(upload_to = "images/")
    views = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title



class Filial(models.Model):
    title = models.CharField(max_length=255)
    established_at = models.DateTimeField()

    def __str__(self):
        return self.title





class Director(models.Model):
    filial = models.OneToOneField(Filial, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()
    age = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to = "images/")


    def __str__(self):
        return self.fullname






