# Generated by Django 4.2.2 on 2023-06-30 00:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_chat_image_chat_upname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日\u3000'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='chat.tag', verbose_name='タグ\u3000\u3000'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='text',
            field=models.TextField(verbose_name='本文\u3000\u3000'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='upname',
            field=models.CharField(default='名無し', max_length=255, verbose_name='名前\u3000\u3000'),
        ),
    ]