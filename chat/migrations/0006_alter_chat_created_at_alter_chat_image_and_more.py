# Generated by Django 4.2.2 on 2023-06-30 02:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_chat_created_at_alter_chat_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ひにち\u3000'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='chat_images/', verbose_name='しゃしん'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='text',
            field=models.TextField(verbose_name='ほんぶん'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='title',
            field=models.CharField(max_length=255, verbose_name='たいとる'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='upname',
            field=models.CharField(default='名無し', max_length=255, verbose_name='おなまえ'),
        ),
    ]