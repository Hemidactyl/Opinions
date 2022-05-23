# Generated by Django 4.0.4 on 2022-05-02 14:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('opinions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 2, 14, 54, 14, 140102, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 2, 14, 54, 14, 114016, tzinfo=utc)),
        ),
    ]
