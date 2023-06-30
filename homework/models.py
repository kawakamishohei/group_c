from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField('きょうか', max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    date = models.DateTimeField('日付', default=timezone.now)
    title = models.CharField('教科', max_length=255)
    text = models.TextField('内容')
    def __str__(self):
        return self.name

class Homework(models.Model):
    image = models.ImageField('しゅくだい', blank=True, null=True, upload_to='homework_images/')
    name = models.CharField('〇ねん〇くみな〇ばん　なまえ', max_length=255, null=True)
    category = models.ForeignKey(
        Category, verbose_name='きょうか',blank=True, null=True,
        on_delete=models.PROTECT)



