# Generated by Django 2.2.5 on 2019-10-03 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191002_0031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='langauge',
            new_name='language',
        ),
    ]
