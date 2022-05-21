from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
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
        product_count = products.count()
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        product_count = products.count()
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

    template_name = "store/index.html"
    context = {'products': paged_products, 'product_count': product_count}
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


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by(
                '-created_at'
            ).filter(Q(description__icontains=keyword) | Q(name__icontains=keyword))
            product_count = products.count()
        else:
            products = None
            product_count = 0

    template_name = "store/index.html"
    context = {'products': products, 'product_count': product_count}
    return render(request, template_name, context)
