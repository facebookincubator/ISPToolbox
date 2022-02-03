# Generated by Django 3.1.14 on 2022-02-02 20:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0088_auto_20220201_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesspointcoveragebuildings',
            name='task_id',
            field=models.CharField(blank=True, default=None, help_text='Celery ID for the Task that was run', max_length=255, null=True, unique=True, verbose_name='Task ID'),
        ),
        migrations.AlterField(
            model_name='accesspointcoveragebuildings',
            name='hash',
            field=models.CharField(help_text='\n            This hash helps determine if the AP has already been computed.\n        ', max_length=255),
        ),
        migrations.AlterField(
            model_name='accesspointcoveragebuildings',
            name='sector',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='building_coverage', to='workspace.accesspointsector'),
        ),
        migrations.AlterField(
            model_name='accesspointcoveragebuildings',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]