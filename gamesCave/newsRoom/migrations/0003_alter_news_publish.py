# Generated by Django 4.2.2 on 2023-07-15 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsRoom', '0002_alter_news_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 15, 7, 39, 25, 78344, tzinfo=datetime.timezone.utc)),
        ),
    ]
