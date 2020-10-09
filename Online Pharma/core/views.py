from django.shortcuts import render
from .models import Medicine,Order,OrderItem
from django.views.generic import ListView, DetailView, View
import json

def item_list(request):
    context = {
        'items': Medicine.objects.all()
    }
    return render(request, "home-page.html", context)

def history(request):
    return render(request,"history.html")

def cart (request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson','')
        dic = json.loads(items_json)
        thank=True
        #user = self.request.user
        order = Order(order_json=items_json, user=request.user, ordered=thank)
        order.save()
        oid = order.order_id
        #cid = order.user
        print(dic)
        for x,y in dic.items():
            med_id = int(x[2:])
            medi = Medicine(id=med_id)
            qty = int(y[0])
            order_item = OrderItem(order_id=order,medicine_id=medi,qty=qty)
            order_item.save()
        return render(request, "cart.html", {'thank':thank, 'id':id})
    return render(request,"cart.html")

class ItemDetailView(DetailView):
    model = Medicine
    template_name = "product-page.html"
