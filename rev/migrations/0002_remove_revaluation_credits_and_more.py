# Generated by Django 4.1.7 on 2023-04-15 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rev', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revaluation',
            name='Credits',
        ),
        migrations.RemoveField(
            model_name='revaluation',
            name='External_marks',
        ),
        migrations.RemoveField(
            model_name='revaluation',
            name='Grades',
        ),
        migrations.RemoveField(
            model_name='revaluation',
            name='Internal_marks',
        ),
        migrations.RemoveField(
            model_name='revaluation',
            name='Revaluation_Status',
        ),
    ]
