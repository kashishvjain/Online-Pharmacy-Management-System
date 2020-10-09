from django.urls import path, include
from .views import item_list,ItemDetailView,history,cart
app_name = 'core'

urlpatterns = [
    path('', item_list,name = 'item_list'),
    path('history/', history,name = 'history'),
    path('maps/', history,name = 'history'),
    path('cart/', cart,name = 'cart'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
]
