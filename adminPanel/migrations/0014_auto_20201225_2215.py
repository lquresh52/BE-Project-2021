# Generated by Django 3.0 on 2020-12-25 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0013_auto_20201225_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='number_of_question_added',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='test',
            name='quiz_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='createdOn',
            field=models.DateField(default=datetime.datetime(2020, 12, 25, 22, 15, 38, 475982), verbose_name='Posted on'),
        ),
    ]
