# Generated by Django 3.0.4 on 2020-04-11 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=250)),
                ('genre', models.TextField(max_length=250)),
                ('album', models.TextField(max_length=250)),
                ('artist', models.TextField(max_length=250)),
            ],
        ),
    ]