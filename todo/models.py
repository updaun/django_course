from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name

# migration -> python SQL문
# database에는 아직 테이블이 없음

# migrate -> python SQL문 -> database에 테이블 생성

# TODO모델에 새로운 항목 추가 시 migrate 다시 해야함