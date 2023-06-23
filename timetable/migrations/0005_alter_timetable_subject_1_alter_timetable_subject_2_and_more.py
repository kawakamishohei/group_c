# Generated by Django 4.2.2 on 2023-06-23 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0004_timetable_subject_2_timetable_subject_3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='subject_1',
            field=models.ForeignKey(default='国語', on_delete=django.db.models.deletion.PROTECT, related_name='FirstPeriod', to='timetable.subject', verbose_name='1限'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_2',
            field=models.ForeignKey(default='国語', on_delete=django.db.models.deletion.PROTECT, related_name='SecondPeriod', to='timetable.subject', verbose_name='2限'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_3',
            field=models.ForeignKey(default='国語', on_delete=django.db.models.deletion.PROTECT, related_name='ThirdPeriod', to='timetable.subject', verbose_name='3限'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_4',
            field=models.ForeignKey(default='国語', on_delete=django.db.models.deletion.PROTECT, related_name='FourthPeriod', to='timetable.subject', verbose_name='4限'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_5',
            field=models.ForeignKey(default='国語', on_delete=django.db.models.deletion.PROTECT, related_name='FifthPeriod', to='timetable.subject', verbose_name='5限'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_6',
            field=models.ForeignKey(default='国語', on_delete=django.db.models.deletion.PROTECT, related_name='SixthPeriod', to='timetable.subject', verbose_name='6限'),
        ),
    ]