# Generated by Django 3.2.6 on 2021-11-02 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bars', '0010_auto_20211102_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar',
            name='current_capacity',
            field=models.IntegerField(default=0),
        ),
    ]
