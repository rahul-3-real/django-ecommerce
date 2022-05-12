from pyexpat import model
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    excerpt = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="categories/%Y/%m/%d/", blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def str(self):
        return f'{self.name}'
