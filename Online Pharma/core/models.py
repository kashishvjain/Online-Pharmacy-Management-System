from django.db import models
from django.conf import settings


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name





class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
   
    
    ordered_date = models.DateTimeField()
