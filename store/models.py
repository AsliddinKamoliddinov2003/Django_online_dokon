from django.db import models
from datetime import datetime, timezone
from django.conf import settings

class Category(models.Model):
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"


    name = models.CharField(verbose_name="Nomi",max_length=255)
    icon=models.ImageField(upload_to="images/",null=True)
    


    created_at = models.DateTimeField(verbose_name="yaratilgan sana",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="O'zgartirilgan sana",auto_now=True)
    slug = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    class Meta:
        verbose_name="Kichik kategoriya"
        verbose_name_plural="Kichik kategoriyalar"

    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=255,null=True)

    

    def __str__(self):
   
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"


    title = models.CharField(max_length=255)
    price = models.FloatField()
    slug = models.CharField(max_length=255,null=True)
    description = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to="images/",null=True)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True)
    is_active = models.BooleanField(default=True)
    


    created_at = models.DateTimeField(auto_now_add = True, null=True)
    updated_at = models.DateTimeField(auto_now = True, null=True)


    def __str__(self):
        return f"{self.title} - {self.price}"


    def get_rating_percent(self):
        return 100 * (self.rating/5)


    def is_new_product(self):
        time_delta = datetime.now(timezone.utc) - self.created_at
        return time_delta.seconds < settings.NEW_PRODUCT_SECONDS



class  Product_color(models.Model):
    name = models.CharField(max_length=255)


class Product_size(models.Model):
    name = models.CharField(max_length=255)


class Product_image(models.Model):
    image = models.ImageField(upload_to="images/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)