# Generated by Django 4.2.2 on 2023-06-12 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_project_left_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='status',
            new_name='is_complete_status',
        ),
    ]
