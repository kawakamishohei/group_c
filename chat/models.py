from django.db import models
from django.utils import timezone
# Create your models here.
class Chat(models.Model):
    name = models.CharField('名前', default='名無し',max_length=255)
    text = models.TextField('コメント内容')
    # target = models.ForeignKey(
    #     Article, on_delete=models.SET_NULL,
    #     blank=True, null=True,
    #     verbose_name='紐づく記事'
    # )