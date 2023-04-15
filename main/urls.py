from django.urls import path
from .views import *

urlpatterns = [
    path('',HomePage,name='home'),
    path('category-list/',category_list,name='category-list'),
    path('brand-list/',brand_list,name='brand-list'),
    path('product-list/',product_list,name='product-list'),
    path('category-product-list/<str:pk>/',category_product_list,name='category-product-list'),
    path('brand-product-list/<str:pk>/',brand_product_list,name='brand-product-list'),

    path('product-details/<slug:slug>/<str:pk>/',product_details,name='product-details'),
    path('search/',search,name='search'),
]
