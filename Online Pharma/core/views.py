from django.shortcuts import render
from .models import Medicine
from django.views.generic import ListView, DetailView, View


def item_list(request):
    context = {
        'items': Medicine.objects.all()
    }
    return render(request, "home-page.html", context)

class ItemDetailView(DetailView):
    model = Medicine
    template_name = "product-page.html"
