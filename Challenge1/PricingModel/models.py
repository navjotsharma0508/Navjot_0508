from django.db import models

# Create your models here.
class Retail(models.Model):
    Store_ID=models.IntegerField()
    SKU=models.CharField(max_length=40)
    Product_name=models.CharField(max_length=50)
    Price=models.IntegerField()
    Date=models.DateField()
