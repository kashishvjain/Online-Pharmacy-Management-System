from django.contrib import admin
from .models import Medicine,Order,OrderItem
# Register your models here.
admin.site.register(Order)
admin.site.register(Medicine)
admin.site.register(OrderItem)
