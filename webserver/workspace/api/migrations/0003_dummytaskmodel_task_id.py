# Generated by Django 3.1.14 on 2022-04-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220407_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='dummytaskmodel',
            name='task_id',
            field=models.CharField(blank=True, default=None, help_text='Celery ID for the Task that was run', max_length=255, null=True, unique=True, verbose_name='Task ID'),
        ),
    ]