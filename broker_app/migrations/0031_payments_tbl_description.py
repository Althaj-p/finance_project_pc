# Generated by Django 3.2.13 on 2022-12-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker_app', '0030_alter_payments_tbl_investor'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments_tbl',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
