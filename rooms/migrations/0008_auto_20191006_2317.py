# Generated by Django 2.2.5 on 2019-10-06 14:17

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_auto_20191006_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='photos', to='rooms.Room'),
        ),
    ]
