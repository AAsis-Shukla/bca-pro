from django.contrib import admin
from .models import *

class Cat(admin.ModelAdmin):
    list_display = ('cat_name','cat_description')
admin.site.register(Category, Cat)

class subCat(admin.ModelAdmin):
    list_display = ('category','subcategory_name','description',)
admin.site.register(Subcategory, subCat)

class Prod(admin.ModelAdmin):
    list_display = ('Prod_name','Prod_image','Prod_desc','category','subcategory',)
    list_display_links = ('Prod_name',)
    search_fields = ('Prod_name', 'Prod_desc')
admin.site.register(Product, Prod)

class LRNAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'rejected_quantity', 'reason', 'rejected_time')

    def product_id(self, obj):
        return obj.product.Prod_id
    product_id.admin_order_field = 'product__Prod_id'
    product_id.short_description = 'Product ID'

admin.site.register(LRN, LRNAdmin)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'phone', 'email', 'company_name', 'address', 'products_supplied')
admin.site.register(Supplier, SupplierAdmin)
