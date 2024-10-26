from django.db import models

# Create your models here.

class Product(models.Model):
    name =models.CharField(max_length=255)
    description = models.TextField( blank=True )


class Thums(models.MOdels):
    Product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product/images/', blank=True,default='')
    image_url = models.CharField(max_length=255,blank = True, default='')
    public_id = models.CharField(max_length=255,blank= True ,default = '')
    

