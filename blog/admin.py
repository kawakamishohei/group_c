from django.contrib import admin

from blog.models import Article, Category, Tag, Comment

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
# Register your models here.
