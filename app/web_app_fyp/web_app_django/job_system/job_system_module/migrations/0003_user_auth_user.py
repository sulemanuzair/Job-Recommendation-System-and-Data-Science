# Generated by Django 3.0.3 on 2020-05-10 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_system_module', '0002_auto_20200419_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]