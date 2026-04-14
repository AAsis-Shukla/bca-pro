from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PrimaryPageContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=12) 
    message = models.TextField()
    def __ste__(self):
        return self.name
    
class PrimaryUserSignUp(models.Model):
    ROLES = (
        ('Admin', 'Admin'),
        ('Guest', 'Guest'),
        ('IO', 'I/O'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)  # Assuming xxx-xxx-xxxx format for simplicity
    email = models.EmailField()
    role = models.CharField(max_length=10, choices=ROLES, default='Guest')
    signUpTime = models.DateTimeField(auto_now_add=True)
    profile_img = models.ImageField(upload_to='User_profile_image/', default=None, max_length=300)

    def __str__(self):
        return self.user.username
    
class Product_Entry(models.Model):
    ch = (
        ('in', 'in'),
        ('out', 'out'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Product_name = models.TextField(max_length = 200)
    Product_image = models.ImageField(upload_to = "Product_Entry_Image",max_length=250,default=None)
    Product_id = models.IntegerField(default=None,null=False)
    Product_quantity = models.IntegerField(null=False)
    Product_inOut = models.CharField(max_length=10, choices=ch, default='out')