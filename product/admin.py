from django.contrib import admin

from .models import Product, ProductImage, Color, Size

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['seller','title','slug','description','price','quantity','category','color','size']
    inlines = [ProductImageAdmin]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product','image']

# Register your models here.
#
# admin.site.register(Product)
# admin.site.register(ProductImage)
admin.site.register(Color)
admin.site.register(Size)
