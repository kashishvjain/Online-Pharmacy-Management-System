from django.shortcuts import render
from .models import Medicine


def item_list(request):
    context = {
        'items': Medicine.objects.all()
    }
    return render(request, "home-page.html", context)

def product(request):
    context = {
        
    }
    return render(request, "product-page.html", context)