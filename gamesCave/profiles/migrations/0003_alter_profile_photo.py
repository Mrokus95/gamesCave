# Generated by Django 4.2.2 on 2023-07-11 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_bank_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='users/avatars/anonymous.png', upload_to='users/avatars/'),
        ),
    ]
