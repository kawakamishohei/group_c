from django.contrib import admin
from chat.models import Chat,Category, Tag, Comment

# Register your models here.
admin.site.register(Chat)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)