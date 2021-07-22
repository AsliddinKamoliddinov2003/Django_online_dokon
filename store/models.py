from django.db import models


# class User(models.Model):
#     firstname = models.CharField(max_length=255)
#     lastname = models.CharField(max_length=255)
#     gmail = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=255,null=True)
#     password = models.CharField(max_length=255)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=True)



class Category(models.Model):
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"


    name = models.CharField(verbose_name="Nomi",max_length=255)
    icon=models.ImageField(upload_to="images/",null=True)
    


    created_at = models.DateTimeField(verbose_name="yaratilgan sana",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="O'zgartirilgan sana",auto_now=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    class Meta:
        verbose_name="Kichik kategoriya"
        verbose_name_plural="Kichik kategoriyalar"

    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

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
    


    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)


    def __str__(self):
        return f"{self.title} - {self.price}"

    def get_rating_percent(self):
        return 100 * (self.rating/5)


