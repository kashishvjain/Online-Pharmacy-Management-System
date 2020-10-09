from django.contrib import admin
from .models import Medicine,Order,OrderItem
from django.contrib.auth.admin import UserAdmin
from .models import User
UserAdmin.fieldsets += ('Custom fields set', {'fields': ('age', 'phone','address','gender')}),
# Register your models here.
admin.site.register(Order)
admin.site.register(Medicine)
admin.site.register(OrderItem)
admin.site.register(User, UserAdmin)
