from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('search/', views.search, name="search"),
    path('category/<slug:slug>/', views.store, name="category-store"),
    path('category/<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name="product-detail"),
]
