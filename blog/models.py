from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='blogs')#user.blogs 어떤 유저의 블로그들을 모두 볼 수 있음
    view = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField('category.Category', related_name='blogs', blank=True) # c = Category.object.get(name="과학") -> c.blogs (기본값 c.set_blog) 가져오기 가능, blank True로 카테고리 설정없이 저장 가능
    hidden = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} ({self.id})"