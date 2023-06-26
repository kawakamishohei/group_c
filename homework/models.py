from django.db import models
from django.utils import timezone


class Post(models.Model):
    date = models.DateTimeField('日付', default=timezone.now)
    title = models.CharField('教科', max_length=255)
    text = models.TextField('内容')
    def __str__(self):
        return self.name
