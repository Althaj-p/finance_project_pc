# Generated by Django 3.2.13 on 2022-12-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker_app', '0025_delete_multiple_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profit_tbl',
            name='projects',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
