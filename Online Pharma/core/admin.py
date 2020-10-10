from django.contrib import admin
from .models import Medicine,Order,OrderItem,Pharmacy,Address
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','age','phone','address','gender')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

# Register your models here.
admin.site.register(Order)
admin.site.register(Medicine)
admin.site.register(OrderItem)
admin.site.register(Pharmacy)
admin.site.register(Address)
# admin.site.register(User, UserAdmin)
admin.site.register(get_user_model(), CustomUserAdmin)
