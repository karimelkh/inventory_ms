from django.shortcuts import render
from . import models

def home(req):
    username = req.user.username
    prods = models.Product.objects.all()
    i_count = models.Product.objects.count()
    c_count = models.Category.objects.count()
    s_count = models.Supplier.objects.count()
    l_count = models.Location.objects.count()
    prod_data = [
        {
            'id_prod': prod.id_prod,
            'prod_title': prod.prod_title,
            'prod_desc': prod.prod_desc,
            'qty_in_stock': prod.qty_in_stock,
            'cat_id': prod.cat_id,
            'locat_id': prod.locat_id,
            'suppl_id': prod.suppl_id
        }
        for prod in prods
    ]
    home_dict = {
        "prod_data": prod_data,
        "username": username,
        "items_count": i_count,
        "cats_count": c_count,
        "suppls_count": s_count,
        "locats_count": l_count,
        # "orders_count": ,
    }
    return render(req, 'main/home.html', home_dict)

#def home(req):
#   prod_ids_list = models.Product.objects.values_list('id_prod', flat=True)
#   prod_obj = models.Product.objects
#   home_dict = { "prod_ids": prod_ids_list, "prod_obj": prod_obj }
#   return render(req, 'main/home.html', home_dict)

def items(req, id):
    items_dict = {}
    return render(req, 'main/items.html', items_dict)

def login(req):
    return render(req, 'main/login.html')
