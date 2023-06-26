from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('タグ名', max_length=255)

    def __str__(self):
        return self.name

class Chat(models.Model):
    title = models.CharField('タイトル', max_length=255)
    upname = models.CharField('名前', default='名無し', max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    category = models.ForeignKey(Category, blank=True, null=True,on_delete=models.PROTECT, verbose_name='カテゴリ')
    image = models.ImageField('投稿画像', null=True, blank=True, upload_to='chat_images/')
    # タグは複数紐づく。また、タグを設定しないことも可能にしている(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True, verbose_name='タグ')

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField('名前', default='名無し',max_length=255)
    text = models.TextField('コメント内容')
    target = models.ForeignKey(
        Chat, on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name='紐づく記事'
    )