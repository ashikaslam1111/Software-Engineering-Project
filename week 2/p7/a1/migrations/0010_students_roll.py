# Generated by Django 4.2.6 on 2023-11-09 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0009_remove_students_roll'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='roll',
            field=models.IntegerField(default=0),
        ),
    ]
