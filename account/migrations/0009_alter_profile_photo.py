# Generated by Django 4.1.3 on 2022-12-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='images/profile2.png', upload_to='users/%Y/%m/%d/'),
        ),
    ]