# Generated by Django 3.1.13 on 2021-11-04 00:03

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IspToolboxApp', '0004_mlabuszip1052020_standardizedmlab_standardizedpostal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gadm36Bra2',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('gid_0', models.CharField(blank=True, max_length=80, null=True)),
                ('name_0', models.CharField(blank=True, max_length=80, null=True)),
                ('gid_1', models.CharField(blank=True, max_length=80, null=True)),
                ('name_1', models.CharField(blank=True, max_length=80, null=True)),
                ('nl_name_1', models.CharField(blank=True, max_length=80, null=True)),
                ('gid_2', models.CharField(blank=True, max_length=80, null=True)),
                ('name_2', models.CharField(blank=True, max_length=80, null=True)),
                ('varname_2', models.CharField(blank=True, max_length=80, null=True)),
                ('nl_name_2', models.CharField(blank=True, max_length=80, null=True)),
                ('type_2', models.CharField(blank=True, max_length=80, null=True)),
                ('engtype_2', models.CharField(blank=True, max_length=80, null=True)),
                ('cc_2', models.CharField(blank=True, max_length=80, null=True)),
                ('hasc_2', models.CharField(blank=True, max_length=80, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'gadm36_bra_2',
                'managed': False,
            },
        ),
    ]
