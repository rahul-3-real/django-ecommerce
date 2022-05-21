from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('<slug:slug>/', views.store, name="category-store"),
    path('<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name="product-detail"),
]
