# Generated by Django 4.2.2 on 2023-07-19 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsRoom', '0010_news_tags_alter_news_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 19, 19, 54, 22, 204124, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=9),
        ),
    ]
