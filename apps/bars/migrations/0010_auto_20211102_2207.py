# Generated by Django 3.2.6 on 2021-11-02 22:07

import apps.bars.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bars', '0009_bar_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='image_file',
            field=models.ImageField(blank=True, default='/Users/christiancapeans/Documents/Glub/glub-api/mediabaricons/default_image.png', upload_to=apps.bars.models.upload_to),
        ),
        migrations.AlterField(
            model_name='bar',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
