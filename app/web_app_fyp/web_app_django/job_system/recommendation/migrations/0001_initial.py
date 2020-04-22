# Generated by Django 3.0.3 on 2020-04-14 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job_system_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopAppliedJobs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('applications_count', models.IntegerField()),
                ('job_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job_system_module.Job')),
            ],
        ),
    ]