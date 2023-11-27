from django.db import models
import random

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    logo = models.CharField(max_length=150, null=True, blank=True)
    website = models.CharField(max_length=150, null=True, blank=True)
    hidden = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.name} {{self.id}}"
    
    def save(self, *args, **kwargs):

        # 처음 생성될 때, 이미지에 값이 없을 경우, 더미 이미지를 넣어준다.
        if not self.id and not self.logo:
            random_number = random.randint(1, 10000)
            self.logo = f"https://picsum.photos/500?random={random_number}"

        super().save(*args, **kwargs)