from django.db import models
import random

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
    
    
    def save(self, *args, **kwargs):
        
        if not self.id and not self.image:
            random_number = random.randint(1, 10000)
            self.image = "https://picsum.photos/500?random={random_number}"
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} ({self.id})"