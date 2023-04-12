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
    categories = Product.objects.distinct().values('category__title','category__id')
    brands = Product.objects.distinct().values('brand__title','brand__id')
    colors = ProductAttribute.objects.distinct().values('color__title','color__id','color__color_code')
    sizes = ProductAttribute.objects.distinct().values('size__title','size__id')

    context = {'products':products,'categories':categories,'brands':brands,'colors':colors,'sizes':sizes}
    return render(request,'main/product_list.html',context)


def category_product_list(request,pk):
    category = Category.objects.get(id=pk)
    category_product = Product.objects.filter(category=category).order_by('-id')

    categories = Product.objects.distinct().values('category__title','category__id')
    brands = Product.objects.distinct().values('brand__title','brand__id')
    colors = ProductAttribute.objects.distinct().values('color__title','color__id','color__color_code')
    sizes = ProductAttribute.objects.distinct().values('size__title','size__id')


    context = {'category_product': category_product,'category':category,'categories':categories,'brands':brands,'colors':colors,'sizes':sizes}
    return render(request,'main/category_product.html',context)


def brand_product_list(request,pk):
    brand = Brand.objects.get(id=pk)
    brand_product = Product.objects.filter(brand=brand).order_by('-id')

    categories = Product.objects.distinct().values('category__title','category__id')
    brands = Product.objects.distinct().values('brand__title','brand__id')
    colors = ProductAttribute.objects.distinct().values('color__title','color__id','color__color_code')
    sizes = ProductAttribute.objects.distinct().values('size__title','size__id')


    context = {'brand_product': brand_product,'brand':brand,'categories':categories,'brands':brands,'colors':colors,'sizes':sizes}
    return render(request,'main/brand_product.html',context)
