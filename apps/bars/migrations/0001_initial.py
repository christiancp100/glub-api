# Generated by Django 3.2.6 on 2021-11-26 18:10

import apps.bars.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous Bar', max_length=60)),
                ('address', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(default=100)),
                ('current_capacity', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=apps.bars.models.upload_to)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('name', 'owner')},
            },
        ),
        migrations.CreateModel(
            name='BarImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.bars.models.upload_to_bar_images_folder)),
                ('description', models.CharField(max_length=100)),
                ('bar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bars.bar')),
            ],
        ),
    ]
