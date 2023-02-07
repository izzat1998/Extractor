from enum import unique

from django.contrib.auth.models import User
from django.db import models
from simple_history.models import HistoricalRecords


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    vote = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField(Category)
    history = HistoricalRecords()
    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.title} - {self.content}'
