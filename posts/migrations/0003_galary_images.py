# Generated by Django 2.2 on 2020-07-12 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_galary_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='galary',
            name='images',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
