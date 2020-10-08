from django.urls import path, include
from .views import item_list,ItemDetailView
app_name = 'core'

urlpatterns = [
    path('', item_list,name = 'item_list'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
]
