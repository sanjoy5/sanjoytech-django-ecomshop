from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class Banner(models.Model):
    img = models.ImageField(upload_to='banner_imgs/',)
    alt = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = '1. Banners'

    def image_tag(self):
        return mark_safe('<img src="%s" width="60" height="30" />' % (self.img.url))
    
    def __str__(self):
        return self.alt

class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cat_imgs/')

    class Meta:
        verbose_name_plural = '2. Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title
    
class Brand(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='brand_imgs/')

    class Meta:
        verbose_name_plural = '3. Brands'

    def image_tag(self):
        return mark_safe('<img src="%s" width="60" height="30" />' % (self.image.url))

    def __str__(self):
        return self.title
    
class Color(models.Model):
    title = models.CharField(max_length=200)
    color_code = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = '4. Colors'

    def color_bg(self):
        return mark_safe('<div style="width:60px; height:20px; background:%s"></div>' % (self.color_code))


    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = '5. Sizes'

    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_imgs/')
    slug = models.CharField(max_length=300)
    details = models.TextField()
    specs = models.TextField()
    price = models.PositiveIntegerField(blank=True,null=True)
    old_price = models.PositiveIntegerField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    brand = models.ForeignKey(Brand,on_delete=models.SET_NULL,null=True,blank=True)
    color = models.ForeignKey(Color,on_delete=models.SET_NULL,null=True,blank=True)
    size = models.ForeignKey(Size,on_delete=models.SET_NULL,null=True,blank=True)
    status = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '6. Products'

    def __str__(self):
        return self.title
    
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    color = models.ForeignKey(Color,on_delete=models.SET_NULL,null=True,blank=True)
    size = models.ForeignKey(Size,on_delete=models.SET_NULL,null=True,blank=True)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = '7. ProductAttributes'
    
    def __str__(self):
        return self.product.title
    

    