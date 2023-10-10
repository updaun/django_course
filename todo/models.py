from django.db import models

# Name : max_length 100
# Description : text
# Done : boolean
# star : integer
# updated_at : datetime
# created_at : datetime
# user(FK)
class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str__(self):
        return self.name