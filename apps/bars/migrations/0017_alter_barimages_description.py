# Generated by Django 3.2.6 on 2021-11-20 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bars', '0016_auto_20211120_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barimages',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
