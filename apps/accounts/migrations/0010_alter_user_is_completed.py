# Generated by Django 3.2.6 on 2021-10-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20211001_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_completed',
            field=models.BooleanField(default=True),
        ),
    ]