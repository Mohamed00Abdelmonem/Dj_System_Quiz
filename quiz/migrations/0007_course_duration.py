# Generated by Django 3.0.5 on 2023-09-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_course_year_of_study'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.PositiveIntegerField(default=30),
        ),
    ]
