# Generated by Django 3.1.13 on 2021-12-03 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0064_auto_20211203_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpelocation',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workspace.accesspointsector'),
        ),
        migrations.DeleteModel(
            name='CPESectorLocation',
        ),
    ]