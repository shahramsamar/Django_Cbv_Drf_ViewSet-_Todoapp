# Generated by Django 4.2.13 on 2024-08-30 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_url',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/user.jpeg'),
        ),
    ]