# Generated by Django 4.1.7 on 2023-04-12 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rev', '0004_alter_subject_max_marks_subject_codes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revaluation_copy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hallticket', models.CharField(max_length=20)),
                ('Student_Name', models.CharField(max_length=250)),
                ('Subject_code', models.CharField(max_length=50)),
                ('Subject', models.CharField(max_length=200)),
                ('Internal_marks', models.IntegerField()),
                ('External_marks', models.IntegerField()),
                ('Second_evaluation', models.IntegerField(blank=True, null=True)),
                ('Third_evaluation', models.IntegerField(blank=True, null=True)),
                ('Credits', models.IntegerField()),
                ('Grades', models.CharField(max_length=2)),
            ],
        ),
    ]
