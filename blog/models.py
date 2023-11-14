from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="blogs")
    view = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField('category.Category', related_name='blogs')
    hidden = models.BooleanField(default=False)
    
