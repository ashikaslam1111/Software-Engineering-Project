# Generated by Django 4.2.6 on 2023-11-06 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_store_model',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('catagory', models.CharField(choices=[('Mystery', 'Mystery'), ('Thriller', 'Thriller'), ('Horrror', 'Horrror')], max_length=50)),
                ('first_pub', models.DateTimeField(auto_now_add=True)),
                ('last_pub', models.DateTimeField()),
            ],
        ),
    ]