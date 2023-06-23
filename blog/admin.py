from django.contrib import admin

from blog.models import Kiji, Category, Tag, Comment

admin.site.register(Kiji)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
# Register your models here.
