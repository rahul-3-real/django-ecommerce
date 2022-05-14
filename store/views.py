from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product

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
