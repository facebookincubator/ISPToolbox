# Generated by Django 3.1.13 on 2021-11-17 23:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0057_pointtopointlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointtopointlink',
            name='radio0hgt',
            field=models.FloatField(default=18.29, validators=[django.core.validators.MinValueValidator(0.1, message='Ensure this value is greater than or equal to %(limit_value)s m.'), django.core.validators.MaxValueValidator(1000, message='Ensure this value is less than or equal to %(limit_value)s. m')]),
        ),
        migrations.AddField(
            model_name='pointtopointlink',
            name='radio1hgt',
            field=models.FloatField(default=18.29, validators=[django.core.validators.MinValueValidator(0.1, message='Ensure this value is greater than or equal to %(limit_value)s m.'), django.core.validators.MaxValueValidator(1000, message='Ensure this value is less than or equal to %(limit_value)s. m')]),
        ),
        migrations.AlterField(
            model_name='pointtopointlink',
            name='frequency',
            field=models.FloatField(default=5.4925, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]