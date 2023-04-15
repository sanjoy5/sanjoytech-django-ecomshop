from django.shortcuts import render
from .models import *

# Create your views here.
def HomePage(request):
    banners = Banner.objects.all()
    products = Product.objects.filter(is_featured=True).order_by('-id')
    context = {'banners':banners,'products':products}
    return render(request,'main/home.html',context)

def category_list(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'main/category_list.html',context)

def brand_list(request):
    brands = Brand.objects.all()
    context = {'brands':brands}
    return render(request,'main/brand_list.html',context)

def product_list(request):
    products = Product.objects.all().order_by('-id')

    context = {'products':products}
    return render(request,'main/product_list.html',context)


def category_product_list(request,pk):
    category = Category.objects.get(id=pk)
    category_product = Product.objects.filter(category=category).order_by('-id')



    context = {'category_product': category_product}
    return render(request,'main/category_product.html',context)


def brand_product_list(request,pk):
    brand = Brand.objects.get(id=pk)
    brand_product = Product.objects.filter(brand=brand).order_by('-id')


    context = {'brand_product': brand_product,'brand':brand}
    return render(request,'main/brand_product.html',context)


def product_details(request,slug,pk):
    product = Product.objects.get(id=pk)
    related_products =  Product.objects.filter(category=product.category).exclude(id=pk)[:4]

    context = {'product':product,'related_products':related_products}
    return render(request,'main/product_details.html',context)


def search(request):
    q = request.GET['q']
    products = Product.objects.filter(title__icontains=q).order_by('-id')
    context = {'products':products,'query':q}
    return render(request,'main/search.html',context)