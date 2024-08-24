from products.models import Product
from items.models import Item
from categories.models import Category
from suppliers.models import Supplier
from storagesites.models import Site

def get_count():
    return {
        "products": Product.objects.count(),
        "items": Item.objects.count(),
        "suppliers": Supplier.objects.count(),
        "sites": Site.objects.count(),
        "categories": Category.objects.count(),
        "orders": 0,
    }
