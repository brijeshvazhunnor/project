# Generated by Django 4.1.5 on 2024-06-07 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("exam", "0008_rename_timetable1_timetable"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="prefertable",
            name="room_id",
        ),
    ]
