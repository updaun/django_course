from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    brand = models.ForeignKey('brand.Brand', on_delete=models.PROTECT, null=True, blank=True)
    image = models.CharField(max_length=150, null=True, blank=True)
    link = models.CharField(max_length=150, null=True, blank=True)
    view = models.PositiveBigIntegerField(default=0)
    hidden = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['name', 'brand']