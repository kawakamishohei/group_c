# Generated by Django 4.2.2 on 2023-06-28 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_homework_remove_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='おなまえ')),
            ],
        ),
    ]
