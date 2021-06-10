# Generated by Django 3.1.10 on 2021-06-10 22:27

from django.db import migrations, models
import storages.backends.s3boto3
import workspace.models.viewshed_models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0020_auto_20210608_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewshedtile',
            name='tile',
            field=models.FileField(storage=storages.backends.s3boto3.S3Boto3Storage(bucket_name='isptoolbox-tilesets', location=''), upload_to=workspace.models.viewshed_models.ViewshedTile.upload_to_path),
        ),
    ]
