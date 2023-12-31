# Generated by Django 4.2.6 on 2023-11-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0002_mytask_desceipsion'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytask',
            name='edit_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mytask',
            name='finished_date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='mytask',
            name='status',
            field=models.CharField(default='INCOMPLETED', max_length=20),
        ),
    ]
