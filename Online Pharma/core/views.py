from django.shortcuts import render
from .models import Medicine


def item_list(request):
    context = {
        'medicines': Medicine.objects.all()
    }
    return render(request, "home-page.html", context)