# Generated by Django 4.1.3 on 2022-12-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]