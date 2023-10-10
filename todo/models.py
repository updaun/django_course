from django.db import models

# Name : max_length 100
# Description : text
# Done : boolean
# Star : Integer
# updated_st : datetime
# created_st : datatime
# User(FK)

# 수정할 때마다 migration 해줘야 함
class Todo(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

    
    
