# Generated by Django 4.2.2 on 2023-06-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_project_task_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='left_amount',
            field=models.FloatField(default=0),
        ),
    ]
