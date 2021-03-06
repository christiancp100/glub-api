# Generated by Django 3.2.6 on 2021-12-20 16:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bars", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                ("description", models.CharField(blank=True, max_length=500)),
                ("start_date", models.DateTimeField()),
                ("finish_date", models.DateTimeField()),
                ("capacity", models.IntegerField()),
                ("is_active", models.BooleanField(default=True)),
                (
                    "bar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="bars.bar"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
