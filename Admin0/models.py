from django.db import models

class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_description = models.TextField()

    def __str__(self):
        return self.cat_name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.subcategory_name

class Product(models.Model):
    Prod_name = models.CharField(max_length=100)
    Prod_image = models.ImageField(upload_to='products/')
    Prod_id = models.IntegerField(default=None, unique=True)
    Prod_desc = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Prod_name

class LRN(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rejected_quantity = models.IntegerField()
    reason = models.TextField()
    rejected_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"LRN for Product ID {self.product.Prod_id} - {self.rejected_quantity} units rejected"

    class Meta:     
        ordering = ['rejected_time']

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    address = models.TextField()
    products_supplied = models.ForeignKey(Product, related_name='suppliers', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.supplier_name
