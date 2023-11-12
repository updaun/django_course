from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True) # 중복이름 x
    logo = models.CharField(max_length=150, blank=True, null=True) # https://wwww.brandcrowd.com/maker/tag/letter.jpg
    website = models.CharField(max_length=150, blank=True, null=True)
    hidden = models.BooleanField(default=False)
    
    