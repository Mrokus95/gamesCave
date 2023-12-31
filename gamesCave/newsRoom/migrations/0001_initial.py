# Generated by Django 4.2.2 on 2023-07-15 07:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0003_alter_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='news/main_images/')),
                ('publish', models.DateTimeField(default=datetime.datetime(2023, 7, 15, 7, 33, 59, 596324, tzinfo=datetime.timezone.utc))),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], max_length=9)),
                ('author', models.ForeignKey(default='Anonymous', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='news', to='profiles.profile', to_field='nick')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
