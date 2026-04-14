from django.contrib import admin

# Register your models here.
from primary.models import *

class adminPPContact(admin.ModelAdmin):
    list_display = ('name','email','number','message')
admin.site.register(PrimaryPageContact,adminPPContact)

class adminPUSignUp(admin.ModelAdmin):
    list_display = (
                    'name',
                    'phone',
                    'email',
                    'role',
                    'signUpTime',
                    'profile_img'
    )
admin.site.register(PrimaryUserSignUp,adminPUSignUp)
class adminPEntry(admin.ModelAdmin):
    list_display = (
                    'user',
                    'Product_name',
                    'Product_image',
                    'Product_id',
                    'Product_quantity',
                    'Product_inOut'
    )
admin.site.register(Product_Entry,adminPEntry)