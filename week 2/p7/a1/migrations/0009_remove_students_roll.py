# Generated by Django 4.2.6 on 2023-11-09 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0008_students_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='roll',
        ),
    ]