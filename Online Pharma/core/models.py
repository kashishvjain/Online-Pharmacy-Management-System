from django.db import models
from django.conf import settings
from django.shortcuts import reverse


class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100,default='None')
    price = models.FloatField()
    stock = models.IntegerField(default=1)
    effects = models.CharField(max_length=100,default='None')
    side_effects = models.CharField(max_length=100,default='None')
    slug = models.SlugField(default=1,unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })





class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)


    ordered_date = models.DateTimeField()
