# Generated by Django 4.2.2 on 2023-06-12 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_rename_task_id_project_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='left_amount',
            field=models.FloatField(),
        ),
    ]