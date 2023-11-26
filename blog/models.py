from django.db import models
import random


class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="blogs")
    view = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField('category.Category', related_name='blogs', blank=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.id})"
    
    def save(self, *args, **kwargs):

        # 처음 생성될 때, 이미지에 값이 없을 경우, 더미 이미지를 넣어준다.
        if not self.id and not self.image:
            random_number = random.randint(1, 10000)
            self.image = f"https://picsum.photos/500?random={random_number}"
        
        super().save(*args, **kwargs)
