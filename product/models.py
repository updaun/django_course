from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank=True) # 일단 넘어가 ㅋㅋㅋㅋ
    price = models.PositiveIntegerField(default=0) # 정수값만
    brand = models.ForeignKey('brand.Brand', on_delete=models.PROTECT, null=True, blank=True) # 상품 존재시 삭제 불가(brand에서 hidden 처리 가능)
    image = models.CharField(max_length=150, null=True, blank=True)
    link = models.CharField(max_length=150, null=True, blank=True)
    view = models.PositiveIntegerField(default=0)
    hidden = models.BooleanField(default=False)

    class Meta:
        unique_together = ["name", "brand"]