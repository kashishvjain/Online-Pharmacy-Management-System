from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


class Address(models.Model):
    apartment_address = models.CharField(max_length=100,default='')
    street_address = models.CharField(max_length=100,default='')
    country =  models.CharField(max_length=100,default='')
    zip = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.zip


class Pharmacy(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name


class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100,default='None')
    price = models.FloatField()
    stock = models.IntegerField(default=1)
    effects = models.CharField(max_length=100,default='None')
    side_effects = models.CharField(max_length=100,default='None')
    slug = models.SlugField(default=1,unique=True)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })



class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    order_json = models.CharField(max_length=1000,default='')
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(auto_now_add=True)



class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)


class User(AbstractUser):
    age = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=30,blank=True)
    gender = models.CharField(max_length=30,blank=True)
