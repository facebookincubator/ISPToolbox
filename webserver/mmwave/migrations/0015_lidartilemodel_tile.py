# Generated by Django 3.1.8 on 2021-06-07 22:41

from django.db import migrations, models
import storages.backends.s3boto3


class Migration(migrations.Migration):

    dependencies = [
        ('mmwave', '0014_merge_20210519_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='lidartilemodel',
            name='tile',
            field=models.FileField(default=None, storage=storages.backends.s3boto3.S3Boto3Storage(bucket_name='isptoolbox-export-file'), upload_to=''),
            preserve_default=False,
        ),
    ]