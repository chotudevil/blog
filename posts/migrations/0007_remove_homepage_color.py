# Generated by Django 2.2 on 2020-07-12 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_homepage_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='color',
        ),
    ]
