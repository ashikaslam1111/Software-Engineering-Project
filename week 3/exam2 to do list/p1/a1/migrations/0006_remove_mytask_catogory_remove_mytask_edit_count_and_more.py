# Generated by Django 4.2.6 on 2023-11-15 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0005_remove_mytask_finished_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mytask',
            name='catogory',
        ),
        migrations.RemoveField(
            model_name='mytask',
            name='edit_count',
        ),
        migrations.RemoveField(
            model_name='mytask',
            name='first_date',
        ),
        migrations.RemoveField(
            model_name='mytask',
            name='last_eidt',
        ),
        migrations.RemoveField(
            model_name='mytask',
            name='status',
        ),
    ]