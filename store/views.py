from django.shortcuts import get_object_or_404, render
from cart.models import Cart, CartItem
from category.models import Category
from .models import Product
from cart.views import _cart_id

# Create your views here.


def store(request, slug=None):
    category = None
    products = None

    if slug != None:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.all().filter(
            category=category, is_available=True
        )

    else:
        products = Product.objects.all().filter(is_available=True)
    template_name = "store/index.html"
    context = {'products': products}
    return render(request, template_name, context)


def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(
            category__slug=category_slug, slug=product_slug
        )
        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request), product=product
        ).exists()
    except Exception as e:
        raise e

    template_name = 'store/detail.html'
    context = {'product': product, 'in_cart': in_cart}
    return render(request, template_name, context)
