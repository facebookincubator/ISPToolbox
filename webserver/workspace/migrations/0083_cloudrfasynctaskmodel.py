# Generated by Django 3.1.14 on 2022-01-24 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0082_auto_20220121_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloudRFAsyncTaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(blank=True, default=None, help_text='Celery ID for the Task that was run', max_length=255, null=True, unique=True, verbose_name='Task ID')),
                ('hash', models.CharField(help_text='\n            This hash helps determine if the AP has already been computed.\n        ', max_length=255)),
                ('sector', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cloudrf_task', to='workspace.accesspointsector')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]