# Generated by Django 3.2.13 on 2022-12-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker_app', '0007_alter_profit_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profit',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
