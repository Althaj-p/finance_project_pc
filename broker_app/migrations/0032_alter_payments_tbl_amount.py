# Generated by Django 3.2.13 on 2022-12-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker_app', '0031_payments_tbl_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments_tbl',
            name='amount',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]