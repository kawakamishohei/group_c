# Generated by Django 4.2.2 on 2023-06-26 07:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0008_lunchmenu_remove_timetable_explain_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lunchmenu',
            name='day',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='日付'),
        ),
    ]
