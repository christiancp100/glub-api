# Generated by Django 3.2.6 on 2021-09-29 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210929_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id_number',
            field=models.CharField(default='45845856W', max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
