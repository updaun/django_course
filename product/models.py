from django.db import models
import random


class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True) # 일단 넘어가
    price = models.PositiveIntegerField(default=0)
    brand = models.ForeignKey("brand.Brand", on_delete=models.PROTECT, null=True, blank=True)
    image = models.CharField(max_length=150, null=True, blank=True)
    link = models.CharField(max_length=150, null=True, blank=True)
    view = models.PositiveIntegerField(default=0)
    hidden = models.BooleanField(default=False)

    class Meta:
        unique_together = ["name", "brand"]
    
    def save(self, *args, **kwargs):

        # 처음 생성될 떄, 이미지에 값이 없을 경우, 더미 데이터를 넣어준다.
        if not self.id and not self.image:
            random_number = random.randint(1, 10000)
            self.image = f"https://picsum.photos/500?random={random_number}"

            super().save(*args, **kwargs)