from store.models import Product, SubCategory
from django.db import models
from django.contrib.auth import get_user_model
from parler.models import TranslatableModel, TranslatedFields

from store.models import ProductColor, ProductSize
from accounts.models import User


def generate_cupon_code():
    import random
    import string
    

    available_chars = string.ascii_letters + string.digits
    code = ""

    for i in range(8):
        index = random.randint(0, len(available_chars)-1)
        code += available_chars[index]

    return code

def add_cupon(self):
    code = generate_cupon_code()
    cupons  =Cupon.objects.filter(code=code)


    if not cupons.exists():
        cupon = Cupon(
            code = code,
            stock = self.stock,
            expires_in = self.expires_in
        )

        cupon.save()
        for category in self.category.all():
            cupon.category.add(category)
        cupon.save()
    else:
        add_cupon(self)    

Client = get_user_model()

class Cart(models.Model):
    session_id = models.CharField(max_length=255,null=True)
    is_active = models.BooleanField(default=True)


    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    

class CartItem(TranslatableModel):
    translation = TranslatedFields(
        color = models.CharField(max_length=255, null=True)
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    size = models.CharField(max_length=255, null=True)
    quantity = models.PositiveIntegerField(default=1)

    reduced_price = models.FloatField(blank=True, default=0.0)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def total_price(self):
        if self.reduced_price != 0.0:
            return self.reduced_price * self.quantity
        else:
            return self.product.price * self.quantity

        

    def get_color_name(self):
        color = ProductColor.objects.filter(id=self.color).first()
        if color:
            return color.name
        else:
            None

    def get_size_name(self):
        size = ProductSize.objects.filter(id=self.size).first()
        if size:
            return size.name
        else:
            None

    def get_price(self):
        if self.reduced_price != 0.0:
            return self.reduced_price
        else:
            return self.product.price


class Cupon(models.Model):
    code = models.CharField(max_length=8, blank=True, unique=True)
    stock = models.FloatField()
    expires_in = models.DateTimeField()
    category = models.ManyToManyField(SubCategory)
    is_used = models.BooleanField(default=False, null=True)


    def __str__(self):
        return self.code


class CuponGroup(models.Model):
    count = models.PositiveIntegerField()
    stock = models.FloatField()
    expires_in = models.DateTimeField()
    category = models.ManyToManyField(SubCategory)


    def save(self, *args, **kwargs):
        super(CuponGroup, self).save(*args, **kwargs)
        for i in range(self.count):
            code = generate_cupon_code()
            cupons  =Cupon.objects.filter(code=code)


            if not cupons.exists():
                cupon = Cupon(
                    code = code,
                    stock = self.stock,
                    expires_in = self.expires_in
                )

                cupon.save()
                cupon_group = CuponGroup.objects.get(count=self.count, stock=self.stock,expires_in=self.expires_in)
                cupon.category.add(*cupon_group.category.all())
                cupon.save()
            else:
                add_cupon(self)    


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.product.title

           












    