# Generated by Django 4.1.5 on 2024-06-07 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam", "0005_remove_exam_exam_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="timetable",
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
                ("exam_id", models.IntegerField()),
                ("date", models.DateField()),
                ("course_id", models.IntegerField()),
            ],
        ),
    ]
