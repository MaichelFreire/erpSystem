# Generated by Django 5.0.4 on 2024-05-15 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_taskstatus_employee_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='created',
            new_name='created_at',
        ),
    ]
