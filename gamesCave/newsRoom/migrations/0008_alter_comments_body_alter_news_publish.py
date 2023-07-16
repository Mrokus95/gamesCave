# Generated by Django 4.2.2 on 2023-07-16 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsRoom', '0007_alter_news_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='body',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 16, 18, 23, 2, 812044, tzinfo=datetime.timezone.utc)),
        ),
    ]
