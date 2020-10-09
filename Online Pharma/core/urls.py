from django.urls import path, include
from .views import item_list,ItemDetailView,History,cart
app_name = 'core'

urlpatterns = [
    path('', item_list,name = 'item_list'),
    path('history/',History.as_view(),name = 'history'),
    path('cart/', cart,name = 'cart'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
]
