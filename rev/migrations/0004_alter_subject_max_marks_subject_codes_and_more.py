# Generated by Django 4.1.7 on 2023-04-12 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rev', '0003_subject_max_marks_delete_regulations_19_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject_max_marks',
            name='Subject_codes',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='subject_max_marks',
            name='Subjects',
            field=models.CharField(max_length=50),
        ),
    ]
