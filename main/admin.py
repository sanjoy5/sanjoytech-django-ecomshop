from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Brand)
admin.site.register(Size)

class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt','image_tag')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')

class ColorAdmin(admin.ModelAdmin):
    list_display = ('title','color_bg')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','id','category','brand','status','is_featured')
    list_editable = ('status','is_featured')


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('image_tag','id','product','price','color','size')
    list_display_links = ('id','product')

admin.site.register(Banner,BannerAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductAttribute,ProductAttributeAdmin)

