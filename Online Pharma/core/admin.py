from django.contrib import admin
from .models import OrderItem,Medicine,Order
# Register your models here.
admin.site.register(Order)
admin.site.register(Medicine)
admin.site.register(OrderItem)