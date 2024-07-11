from django.shortcuts import render, redirect
from items.models import Item
from . import models


def home(req):
    if req.user.is_authenticated:
        username = req.user.username
        prods = Item.objects.all()
        i_count = Item.objects.count()
        c_count = models.Category.objects.count()
        s_count = models.Supplier.objects.count()
        l_count = models.Location.objects.count()
        o_count = 0
        prod_data = [
            {
                'id_prod': prod.prod_id,
                'prod_title': prod.prod_title,
                'prod_desc': prod.prod_desc,
                'qty_in_stock': prod.stock,
                'cat_id': prod.cat_id,
                'locat_id': prod.locat_id,
                'suppl_id': prod.suppl_id
            }
            for prod in prods
        ]
        context = {
            "prod_data": prod_data,
            "username": username,
            "items_count": i_count,
            "cats_count": c_count,
            "suppls_count": s_count,
            "locats_count": l_count,
            "orders_count": o_count,
        }
        return render(req, 'main/home.html', context)
    else:
        return redirect("/login/")
