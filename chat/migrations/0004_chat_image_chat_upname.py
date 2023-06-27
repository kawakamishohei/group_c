# Generated by Django 4.2.2 on 2023-06-27 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='chat_images/', verbose_name='投稿画像'),
        ),
        migrations.AddField(
            model_name='chat',
            name='upname',
            field=models.CharField(default='名無し', max_length=255, verbose_name='名前'),
        ),
    ]