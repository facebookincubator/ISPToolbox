# Generated by Django 3.1.13 on 2021-10-18 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IspToolboxAccounts', '0013_staffuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='isptoolboxusersignupinfo',
            name='company_goal',
        ),
        migrations.RemoveField(
            model_name='isptoolboxusersignupinfo',
            name='individual_role',
        ),
    ]
