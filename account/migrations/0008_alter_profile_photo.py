# Generated by Django 4.1.3 on 2022-12-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='static/images/profile2.png', upload_to='users/%Y/%m/%d/'),
        ),
    ]
