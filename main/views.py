from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from . import models
from .forms import LoginForm


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
        "orders_count": "-",
    }
    return render(req, 'main/home.html', home_dict)


def items(req, id):
    items_dict = {}
    return render(req, 'main/items.html', items_dict)


def login_user(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect('/home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(req, 'main/login.html', {'form': form})
