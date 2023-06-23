from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255)

    def __str__(self):
        return self.name




class homework(models.Model):
    title = models.CharField('教科', max_length=255)
    text = models.TextField('提出内容')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')

    def __str__(self):
        return self.title

