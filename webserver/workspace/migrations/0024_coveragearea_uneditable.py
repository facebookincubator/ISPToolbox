# Generated by Django 3.1.12 on 2021-06-22 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0023_auto_20210616_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='coveragearea',
            name='uneditable',
            field=models.BooleanField(default=False),
        ),
    ]