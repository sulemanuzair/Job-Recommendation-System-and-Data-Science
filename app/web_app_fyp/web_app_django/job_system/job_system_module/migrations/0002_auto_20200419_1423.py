# Generated by Django 3.0.3 on 2020-04-19 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_system_module', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplication',
            old_name='job_id',
            new_name='job',
        ),
        migrations.RenameField(
            model_name='jobapplication',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='userhistory',
            old_name='user_id',
            new_name='user',
        ),
    ]