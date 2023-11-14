from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.id})"