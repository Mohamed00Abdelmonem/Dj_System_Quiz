# Generated by Django 3.0.5 on 2023-09-28 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20201209_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='year_of_study',
            field=models.CharField(blank=True, choices=[('one', 'one'), ('two', 'two'), ('three', 'three')], max_length=10, null=True),
        ),
    ]
