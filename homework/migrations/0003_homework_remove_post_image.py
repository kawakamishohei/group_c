# Generated by Django 4.2.2 on 2023-06-27 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='homework_images/', verbose_name='宿題')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]