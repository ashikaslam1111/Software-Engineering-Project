# Generated by Django 4.2.6 on 2023-11-09 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0003_employee_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=40)),
                ('section', models.CharField(max_length=40)),
                ('class_teacher', models.CharField(max_length=60)),
                ('hw', models.BooleanField()),
                ('atendance', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('a1.friend',),
        ),
    ]