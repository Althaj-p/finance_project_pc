# Generated by Django 3.2.13 on 2022-12-07 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('broker_app', '0018_rename_statements_statements_tbl'),
    ]

    operations = [
        migrations.AddField(
            model_name='statements_tbl',
            name='investor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='broker_app.investors'),
        ),
    ]
