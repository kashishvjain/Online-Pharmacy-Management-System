from django.urls import path, include
from .views import item_list,product
app_name = 'core'

urlpatterns = [
    path('', item_list,name = 'item_list'),
    path('product/',product,name = 'product'),
]
