# Generated by Django 3.2.13 on 2022-12-07 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker_app', '0015_auto_20221206_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='share',
            field=models.FloatField(max_length=100, null=True),
        ),
    ]
