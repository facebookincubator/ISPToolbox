# Generated by Django 3.1.13 on 2021-12-06 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0069_auto_20211203_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='aptocpelink',
            name='sector',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='workspace.accesspointsector'),
        ),
        migrations.AlterField(
            model_name='aptocpelink',
            name='ap',
            field=models.ForeignKey(blank=True, default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='workspace.accesspointlocation'),
        ),
    ]