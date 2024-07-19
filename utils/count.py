from items.models import Item
from categories.models import Category
from suppliers.models import Supplier
from storagesites.models import Site

def get_count():
    return {
        "items": Item.objects.count(),
        "suppliers": Supplier.objects.count(),
        "sites": Site.objects.count(),
        "categories": Category.objects.count(),
        "orders": 0,
    }
