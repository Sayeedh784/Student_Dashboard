# Generated by Django 3.2.4 on 2021-06-30 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20210630_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homework',
            old_name='sunject',
            new_name='subject',
        ),
    ]
