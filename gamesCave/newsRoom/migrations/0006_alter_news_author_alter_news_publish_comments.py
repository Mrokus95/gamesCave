# Generated by Django 4.2.2 on 2023-07-16 16:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_photo'),
        ('newsRoom', '0005_alter_news_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(default='Anonymous', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='profile', to='profiles.profile', to_field='nick'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 16, 16, 55, 32, 759708, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('reported', 'Reported'), ('published', 'Published')], default='published', max_length=9)),
                ('author', models.ForeignKey(default='Anonymous', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='comment_profile', to='profiles.profile', to_field='nick')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='newsRoom.news')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
