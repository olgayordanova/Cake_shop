from cake_shop_app.models import Product

def create_product( **kwargs):
    return Product.objects.create(**kwargs)
