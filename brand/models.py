from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    logo = models.CharField(max_length=150, null=True, blank=True)
    website = models.CharField(max_length=150, null=True, blank=True)
    hidden = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.name} {{self.id}}"
