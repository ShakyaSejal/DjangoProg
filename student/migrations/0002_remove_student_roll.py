# Generated by Django 5.0 on 2023-12-15 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='roll',
        ),
    ]
